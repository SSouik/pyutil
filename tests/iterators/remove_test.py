import pytest
from pyutil import remove


def test_remove_with_empty_list():
    actual = list(remove([], 1))
    expected = []
    assert actual == expected


def test_remove_with_empty_tuple():
    actual = list(remove((), 1))
    expected = []
    assert actual == expected


def test_remove_when_seq_has_values():
    actual = list(remove([1, 2, 3], 2))
    expected = [1, 3]
    assert actual == expected


def test_remove_when_seq_has_values_2():
    actual = list(remove(["foo", "bar", "abc", "123"], "foo"))
    expected = ["bar", "abc", "123"]
    assert actual == expected


def test_remove_when_seq_has_values_3():
    actual = list(remove(["foo", "bar", "abc", "123"], "bar", "123"))
    expected = ["foo", "abc"]
    assert actual == expected


def test_remove_when_seq_has_values_4():
    actual = list(remove(({"a": 1}, {"b": 2}, {"c": 3}), {"a": 1}))
    expected = [{"b": 2}, {"c": 3}]
    assert actual == expected


def test_remove_when_seq_has_values_5():
    actual = list(remove([1, 2, 3, 4, 5, 6, 7], 2, 3, 12, 5))
    expected = [1, 4, 6, 7]
    assert actual == expected


def test_remove_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(remove("foo", 1))
