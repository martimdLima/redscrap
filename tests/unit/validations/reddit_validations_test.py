import pytest
from unittest.mock import Mock, patch
from common.validations.reddit_api_validations import RedditApiValidations
from common.exceptions.main_exceptions import SubredditNotFoundException

reddit_api_validations = RedditApiValidations()

@pytest.fixture
def mock_valid_response():
    return {"data": {"children": [{}]}}


@pytest.fixture
def mock_invalid_response():
    return {}

def test_validate_subreddits_list_success():
    reddit_api_validations.validate_subreddit = Mock(return_value=True)
    subreddits = ['python', 'learnprogramming', 'webdev']
    verbose = False
    result = reddit_api_validations.validate_subreddits_list(subreddits)
    assert result is None

def test_validate_subreddits_list_failure():
    reddit_api_validations.validate_subreddit = Mock(return_value=False)
    subreddits = ['fake_subreddit', 'learnprogramming', 'webdev']
    verbose = False
    with pytest.raises(SubredditNotFoundException) as excinfo:
        reddit_api_validations.validate_subreddits_list(subreddits)
    assert str(excinfo.value) == 'The provided subreddit fake_subreddit was not found. Please provide a valid one'
