import pytest
from pyutil import tail


def test_tail_with_empty_list():
    actual = list(tail([]))
    expected = []
    assert actual == expected


def test_tail_with_empty_tuple():
    actual = list(tail(()))
    expected = []
    assert actual == expected


def test_tail_with_values():
    actual = list(tail([1, 2, 3, 4, 5]))
    expected = [2, 3, 4, 5]
    assert actual == expected


def test_tail_with_values_2():
    actual = list(tail([1, 2, 3]))
    expected = [2, 3]
    assert actual == expected


def test_tail_with_values_3():
    actual = list(tail(["abc", "def", "ghi", "jkl"]))
    expected = ["def", "ghi", "jkl"]
    assert actual == expected


def test_tail_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(tail("foo"))
