import unittest
from unittest.mock import MagicMock, patch

from common.exceptions.main_exceptions import TokenErrorException, SubredditNotFoundException, UserNotFoundException      # type: ignore
from core.api.reddit_api import RedditApi       # type: ignore
from common.validations.reddit_api_validations import RedditApiValidations


class TestRedditApi(unittest.TestCase):
    def setUp(self):
        self.client_id = 'my_client_id'
        self.secret_token = 'my_secret_token'
        self.username = 'my_username'
        self.password = 'my_password'
        self.reddit_api = RedditApi(self.client_id, self.secret_token, self.username, self.password)
        self.reddit_api_validations = RedditApiValidations()

    def test_get_reddit_api_token_success(self):
        expected_token = "test_token"
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'access_token': expected_token}
        with patch('requests.post', return_value=mock_response):
            reddit_api = RedditApi(self.client_id, self.secret_token, self.username, self.password)
            token = reddit_api.generate_reddit_api_token()
            self.assertEqual(token, expected_token)

    def test_get_reddit_api_token_failure(self):
        mock_response = MagicMock()
        mock_response.ok = False
        with patch('requests.post', return_value=mock_response):
            reddit_api = RedditApi(self.client_id, self.secret_token, self.username, self.password)
            with self.assertRaises(TokenErrorException):
                reddit_api.generate_reddit_api_token()

    def test_subreddit_exists_valid(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "children": [{}]
            }
        }
        requests = MagicMock(return_value=mock_response)

        with unittest.mock.patch('requests.get', requests):
            self.assertTrue(self.reddit_api_validations.validate_subreddit("python"))

    def test_subreddit_exists_invalid(self):
        mock_response = MagicMock()
        mock_response.status_code = 404
        requests = MagicMock(return_value=mock_response)

        with unittest.mock.patch('requests.get', requests):
            self.assertFalse(self.reddit_api_validations.validate_subreddit("invalid_subreddit"))

    def test_validate_subreddits_valid(self):
        subreddits = ["python", "learnpython"]
        self.reddit_api_validations.validate_subreddit = MagicMock(return_value=True)

        try:
            self.reddit_api_validations.validate_subreddits_list(subreddits)
        except SubredditNotFoundException:
            self.fail("SubredditNotFoundException raised unexpectedly")

    def test_validate_subreddits_invalid(self):
        subreddits = ["invalid_subreddit"]
        self.reddit_api_validations.validate_subreddit = MagicMock(return_value=False)

        with self.assertRaises(SubredditNotFoundException):
            self.reddit_api_validations.validate_subreddits_list(subreddits)

    @patch('requests.get')
    def test_check_if_user_exists_user_exists(self, mock_requests_get):
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = False
        mock_requests_get.return_value = mock_response

        result = self.reddit_api_validations.validate_reddit_user('token', 'reddit_user')

        self.assertFalse(result)

    @patch('requests.get')
    def test_check_if_user_exists_user_does_not_exist(self, mock_requests_get):
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = True
        mock_requests_get.return_value = mock_response

        result = self.reddit_api_validations.validate_reddit_user('token', 'reddit_user')

        self.assertFalse(result)

    @patch('requests.get')
    def test_check_if_user_exists_request_failed(self, mock_requests_get):
        mock_response = MagicMock(status_code=400)
        mock_requests_get.return_value = mock_response

        reddit_api = RedditApi('client_id', 'secret_token', 'username', 'password')
        with self.assertRaises(UserNotFoundException):
            self.reddit_api_validations.validate_reddit_user('token', 'reddit_user')