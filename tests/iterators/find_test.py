import pytest
from pyutil import find

sample_data = [
    {"foo": "abc", "bar": "123"},
    {"foo": "def", "bar": "456"},
    {"foo": "ghi", "bar": "789"},
    {"foo": "jkl", "bar": "100"},
    {"foo": "mno", "bar": "101"},
]


def test_find_when_seq_is_empty_list():
    actual = find([], lambda x: x == True)
    expected = None
    assert actual == expected


def test_find_when_seq_is_empty_tuple():
    actual = find((), lambda x: x == True)
    expected = None
    assert actual == expected


def test_find_when_seq_is_list():
    actual = find(sample_data, lambda x: x["foo"] == "def")
    expected = {"foo": "def", "bar": "456"}
    assert actual == expected


def test_find_when_seq_is_tuple():
    actual = find(tuple(sample_data), lambda x: x["foo"] == "def")
    expected = {"foo": "def", "bar": "456"}
    assert actual == expected


def test_find_when_seq_is_list_with_start_as_1():
    actual = find(sample_data, lambda x: x["foo"] == "def", 1)
    expected = {"foo": "def", "bar": "456"}
    assert actual == expected


def test_find_when_seq_is_tuple_with_start_as_1():
    actual = find(tuple(sample_data), lambda x: x["foo"] == "def", 1)
    expected = {"foo": "def", "bar": "456"}
    assert actual == expected


def test_find_when_seq_is_list_with_start_as_2():
    actual = find(sample_data, lambda x: x["foo"] == "def", 2)
    expected = None
    assert actual == expected


def test_find_when_seq_is_tuple_with_start_as_2():
    actual = find(tuple(sample_data), lambda x: x["foo"] == "def", 2)
    expected = None
    assert actual == expected


def test_find_when_seq_is_list_when_item_is_in_start_end_range():
    actual = find(sample_data, lambda x: x["foo"] == "def", 1, 4)
    expected = {"foo": "def", "bar": "456"}
    assert actual == expected


def test_find_when_seq_is_tuple_when_item_is_in_start_end_range():
    actual = find(tuple(sample_data), lambda x: x["foo"] == "def", 1, 4)
    expected = {"foo": "def", "bar": "456"}
    assert actual == expected


def test_find_when_seq_is_list_when_item_is_not_in_start_end_range():
    actual = find(sample_data, lambda x: x["foo"] == "def", 2, 4)
    expected = None
    assert actual == expected


def test_find_when_seq_is_tuple_when_item_is_not_in_start_end_range():
    actual = find(tuple(sample_data), lambda x: x["foo"] == "def", 2, 4)
    expected = None
    assert actual == expected


def test_find_when_start_and_end_are_equal():
    actual = find(sample_data, lambda x: x["foo"] == "def", 1, 1)
    expected = None
    assert actual == expected


def test_find_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        find("foo", lambda x: x == 0)


def test_find_when_func_is_not_callable():
    with pytest.raises(TypeError):
        find([], "foo")


def test_find_when_start_is_negative():
    with pytest.raises(ValueError):
        find([], lambda x: x == 0, -1)


def test_find_when_end_is_negative():
    with pytest.raises(ValueError):
        find([], lambda x: x == 0, 0, -1)


def test_find_when_start_is_greater_than_end():
    with pytest.raises(ValueError):
        find([], lambda x: x == 2, 1)


def test_find_when_start_is_greater_than_len_of_seq():
    with pytest.raises(ValueError):
        find([], lambda x: x["foo"] == "def", 10)
