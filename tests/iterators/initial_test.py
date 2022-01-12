import pytest
from pyutil import initial


def test_initial_with_empty_list():
    actual = list(initial([]))
    expected = []
    assert actual == expected


def test_initial_with_empty_tuple():
    actual = list(initial(()))
    expected = []
    assert actual == expected


def test_initial_with_empty_set():
    actual = list(initial(set([])))
    expected = []
    assert actual == expected


def test_initial_with_empty_string():
    actual = list(initial(""))
    expected = []
    assert actual == expected


def test_initial_with_list():
    actual = list(initial([1, 2, 3, 4, 5]))
    expected = [1, 2, 3, 4]
    assert actual == expected


def test_initial_with_tuple():
    actual = list(initial((1, 2, 3, 4, 5)))
    expected = [1, 2, 3, 4]
    assert actual == expected


def test_initial_with_set():
    actual = list(initial({1, 2, 3, 4, 5}))
    expected = [1, 2, 3, 4]
    assert actual == expected


def test_initial_with_string():
    actual = list(initial("foobar"))
    expected = ["f", "o", "o", "b", "a"]
    assert actual == expected


def test_initial_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(initial(123))
