import pytest
from pyutil import fill


def test_fill_when_seq_is_empty():
    actual = list(fill([], "a"))
    assert actual == []


def test_fill_when_seq_has_length():
    actual = list(fill([1, 2, 3], "x"))
    expected = ["x", "x", "x"]
    assert actual == expected


def test_fill_when_start_index_is_1():
    actual = list(fill([1, 2, 3], "x", 1))
    expected = [1, "x", "x"]
    assert actual == expected


def test_fill_when_end_index_is_1():
    actual = list(fill([1, 2, 3], "x", 0, 1))
    expected = ["x", 2, 3]
    assert actual == expected


def test_fill_with_start_and_end_index():
    actual = list(fill([1, 2, 3, 4, 5, 6], "x", 2, 5))
    expected = [1, 2, "x", "x", "x", 6]
    assert actual == expected


def test_fill_with_start_and_end_index_equal():
    actual = list(fill([1, 2, 3, 4, 5, 6], "x", 2, 2))
    expected = [1, 2, 3, 4, 5, 6]
    assert actual == expected


def test_fill_when_seq_is_tuple():
    actual = list(fill((1, 2, 3), "x"))
    expected = ["x", "x", "x"]
    assert actual == expected


def test_fill_when_seq_is_set():
    actual = list(fill({1, 2, 3}, "x"))
    expected = ["x", "x", "x"]
    assert actual == expected


def test_fill_when_seq_is_string():
    actual = list(fill("abc", "x"))
    expected = ["x", "x", "x"]
    assert actual == expected


def test_fill_when_start_index_is_negative():
    with pytest.raises(ValueError):
        list(fill([1, 2, 3], "x", -1))


def test_fill_when_end_index_is_negative():
    with pytest.raises(ValueError):
        list(fill([1, 2, 3], "x", 0, -1))


def test_fill_when_start_is_greater_than_end():
    with pytest.raises(ValueError):
        list(fill([1, 2, 3], "x", 5, 2))


def test_fill_when_start_index_is_not_int():
    with pytest.raises(TypeError):
        list(fill([1, 2, 3], "x", "foo"))


def test_fill_when_end_index_is_not_int():
    with pytest.raises(TypeError):
        list(fill([1, 2, 3], "x", 0, "foo"))


def test_fill_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(fill(1, "x"))
