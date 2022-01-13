import pytest
from pyutil import last


def test_last_with_empty_list():
    actual = last([])
    expected = None
    assert actual == expected


def test_last_with_empty_tuple():
    actual = last(())
    expected = None
    assert actual == expected


def test_last_with_empty_string():
    actual = last("")
    expected = None
    assert actual == expected


def test_last_with_list():
    actual = last([1, 2, 3])
    expected = 3
    assert actual == expected


def test_last_with_tuple():
    actual = last((1, 2, 3))
    expected = 3
    assert actual == expected


def test_last_with_empty_string():
    actual = last("abc")
    expected = "c"
    assert actual == expected


def test_last_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        last(123)
