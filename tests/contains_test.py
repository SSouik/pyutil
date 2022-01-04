import pytest
from pyutil.contains import contains


def test_contains_with_empty_list():
    actual = contains([], "foo")
    assert actual == False


def test_contains_with_empty_tuple():
    actual = contains((), "foo")
    assert actual == False


def test_contains_with_empty_dict():
    actual = contains({}, "foo")
    assert actual == False


def test_contains_with_empty_string():
    actual = contains("", "foo")
    assert actual == False


def test_contains_with_int():
    with pytest.raises(TypeError):
        contains(1, "foo")


def test_contains_with_bool():
    with pytest.raises(TypeError):
        contains(True, "foo")


def test_contains_with_callable():
    with pytest.raises(TypeError):
        contains(lambda: 1, "foo")


def test_contains_when_list_has_value():
    actual = contains([1, 2, 3], 2)
    assert actual == True


def test_contains_when_set_has_value():
    actual = contains({1, 2, 3}, 2)
    assert actual == True


def test_contains_when_dict_has_value_as_key():
    actual = contains({"a": 1, "b": 2}, "a")
    assert actual == True


def test_contains_when_dict_has_value_as_value():
    actual = contains({"a": 1, "b": 2}, 1)
    assert actual == True
