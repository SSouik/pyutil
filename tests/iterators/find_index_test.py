import pytest
from pyutil import find_index

sample_data = [
    {"foo": "abc", "bar": "123"},
    {"foo": "def", "bar": "456"},
    {"foo": "ghi", "bar": "789"},
    {"foo": "jkl", "bar": "100"},
    {"foo": "mno", "bar": "101"},
]


def test_find_index_when_seq_is_empty_list():
    actual = find_index([], lambda x: x == 0)
    expected = -1
    assert actual == expected


def test_find_index_when_seq_is_empty_tuple():
    actual = find_index((), lambda x: x == 0)
    expected = -1
    assert actual == expected


def test_find_index_when_seq_is_list():
    actual = find_index(sample_data, lambda x: x["foo"] == "ghi")
    expected = 2
    assert actual == expected


def test_find_index_when_seq_is_tuple():
    actual = find_index(tuple(sample_data), lambda x: x["foo"] == "ghi")
    expected = 2
    assert actual == expected


def test_find_index_when_item_does_not_exist_in_list():
    actual = find_index(sample_data, lambda x: x["foo"] == "123")
    expected = -1
    assert actual == expected


def test_find_index_when_item_does_not_exist_in_list():
    actual = find_index(tuple(sample_data), lambda x: x["foo"] == "123")
    expected = -1
    assert actual == expected


def test_find_index_when_seq_is_list_with_from_index():
    actual = find_index(sample_data, lambda x: x["foo"] == "ghi", 2)
    expected = 2
    assert actual == expected


def test_find_index_when_seq_is_tuple_with_from_index():
    actual = find_index(tuple(sample_data), lambda x: x["foo"] == "ghi", 2)
    expected = 2
    assert actual == expected


def test_find_index_when_item_does_not_exist_in_list_with_from_index():
    actual = find_index(sample_data, lambda x: x["foo"] == "ghi", 3)
    expected = -1
    assert actual == expected


def test_find_index_when_item_does_not_exist_in_tuple_with_from_index():
    actual = find_index(tuple(sample_data), lambda x: x["foo"] == "ghi", 3)
    expected = -1
    assert actual == expected


def test_find_index_when_seq_is_list_with_from_index_is_negative():
    actual = find_index(sample_data, lambda x: x["foo"] == "ghi", -2)
    expected = 2
    assert actual == expected


def test_find_index_when_seq_is_tuple_with_from_index_is_negative():
    actual = find_index(tuple(sample_data), lambda x: x["foo"] == "ghi", -2)
    expected = 2
    assert actual == expected


def test_find_index_when_item_does_not_exist_in_list_with_from_index_is_negative():
    actual = find_index(sample_data, lambda x: x["foo"] == "ghi", -4)
    expected = -1
    assert actual == expected


def test_find_index_when_item_does_not_exist_in_tuple_with_from_index_is_negative():
    actual = find_index(tuple(sample_data), lambda x: x["foo"] == "ghi", -4)
    expected = -1
    assert actual == expected


def test_find_index_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        find_index("foo", lambda x: x == 0)


def test_find_index_when_func_is_not_callable():
    with pytest.raises(TypeError):
        find_index([], "foo")


def test_find_index_when_from_index_is_not_int():
    with pytest.raises(TypeError):
        find_index([], lambda x: x == 0, "foo")
