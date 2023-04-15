import pytest

from common.validations.url_validations import UrlValidations

possible_base_urls = ["ze-robot.com/dl/",
                      "i.redd.it",
                      "https://old.reddit.com/r/",
                      "https://i.imgur.com",
                      "https://static.greatbigcanvas.com"]


@pytest.fixture
def validator():
    return UrlValidations()


def test_valid_url_with_base_url(validator):
    url = "https://i.redd.it/z9gowbfiett61.jpg"
    base_urls = ['i.redd.it']
    assert validator.validate_if_url_is_a_valid_img_link(url, base_urls) is True


def test_valid_url_with_multiple_base_urls(validator):
    url = "https://i.redd.it/z9gowbfiett61.jpg"
    assert validator.validate_if_url_is_a_valid_img_link(url, possible_base_urls) is True


def test_invalid_url_with_base_url(validator):
    url = "https://i.redd.it/z9gowbfiett61.txt"
    base_urls = ["invalid.test.baseurl"]
    assert validator.validate_if_url_is_a_valid_img_link(url, base_urls) is False


def test_invalid_url_with_multiple_base_urls(validator):
    url = 'https://www.not_an_example.com/not_an_image.png'
    assert validator.validate_if_url_is_a_valid_img_link(url, possible_base_urls) is False


def test_invalid_url_without_base_url(validator):
    url = 'https://www.not_an_example.com/not_an_image.png'
    base_urls = ['example.com']
    assert validator.validate_if_url_is_a_valid_img_link(url, base_urls) is False