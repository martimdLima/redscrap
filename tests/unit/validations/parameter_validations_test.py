import pytest

from common.validations.parameter_validations import ParameterValidations

def test_valid_input():
    obj = ParameterValidations()
    input_str = "test,subreddit,python"
    expected_output = ["test", "subreddit", "python"]
    assert obj.validate_subreddits_parameter(input_str) == expected_output


def test_invalid_special_chars():
    obj = ParameterValidations()
    input_str = "test-subreddit;python"
    with pytest.raises(ValueError):
        obj.validate_subreddits_parameter(input_str)


def test_invalid_both_commas_and_semicolons():
    obj = ParameterValidations()
    input_str = "test,subreddit;python,programming"
    with pytest.raises(ValueError):
        obj.validate_subreddits_parameter(input_str)


def test_only_one_subreddit():
    obj = ParameterValidations()
    input_str = "test"
    expected_output = ["test"]
    assert obj.validate_subreddits_parameter(input_str) == expected_output


def test_whitespace_and_empty_values():
    obj = ParameterValidations()
    input_str = "test,   subreddit,   python,,"
    expected_output = ["test", "subreddit", "python"]
    assert obj.validate_subreddits_parameter(input_str) == expected_output