import pytest
from pyutil import remove_all


def test_remove_all_with_empty_list():
    actual = list(remove_all([], [1]))
    expected = []
    assert actual == expected


def test_remove_all_with_empty_tuple():
    actual = list(remove_all((), [1]))
    expected = []
    assert actual == expected


def test_remove_all_when_seq_has_values():
    actual = list(remove_all([1, 2, 3], [2]))
    expected = [1, 3]
    assert actual == expected


def test_remove_all_when_seq_has_values_2():
    actual = list(remove_all(["foo", "bar", "abc", "123"], ["foo"]))
    expected = ["bar", "abc", "123"]
    assert actual == expected


def test_remove_all_when_seq_has_values_3():
    actual = list(remove_all(["foo", "bar", "abc", "123"], ("bar", "123")))
    expected = ["foo", "abc"]
    assert actual == expected


def test_remove_all_when_seq_has_values_4():
    actual = list(remove_all(({"a": 1}, {"b": 2}, {"c": 3}), [{"a": 1}]))
    expected = [{"b": 2}, {"c": 3}]
    assert actual == expected


def test_remove_all_when_seq_has_values_5():
    actual = list(remove_all([1, 2, 3, 4, 5, 6, 7], {2, 3, 12, 5}))
    expected = [1, 4, 6, 7]
    assert actual == expected


def test_remove_all_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(remove_all("foo", [1]))


def test_remove_all_when_remove_vals_is_not_valid():
    with pytest.raises(TypeError):
        list(remove_all([], 1))
