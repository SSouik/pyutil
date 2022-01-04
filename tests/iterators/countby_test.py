import pytest
from pyutil import countby


def test_countby_with_empty_list():
    actual = countby([], "foo")
    expected = {}
    assert actual == expected


def test_countby_with_empty_tuple():
    actual = countby((), "foo")
    expected = {}
    assert actual == expected


def test_countby_with_empty_set():
    actual = countby(set([]), "foo")
    expected = {}
    assert actual == expected


def test_countby_when_key_is_string():
    key = "foo"
    lst = [
        {"foo": "bar"},
        {"foo": "foo"},
        {"foo": "foo"},
        {"foo": "bar"},
        {"foo": "bar"},
        {"foo": "bar"},
    ]

    actual = countby(lst, key)
    expected = {"foo": 2, "bar": 4}

    assert actual == expected


def test_countby_when_key_is_callabe():
    def even_odd(x):
        if x % 2 == 0:
            return "even"
        return "odd"

    lst = [1, 2, 3, 4, 5, 6, 7]

    actual = countby(lst, even_odd)
    expected = {"even": 3, "odd": 4}

    assert actual == expected


def test_countby_when_key_is_callabe_2():
    def length(x):
        return len(x)

    lst = ["one", "two", "three", "four", "five"]

    actual = countby(lst, length)
    expected = {3: 2, 4: 2, 5: 1}

    assert actual == expected


def test_countby_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        countby("foo", "foo")
