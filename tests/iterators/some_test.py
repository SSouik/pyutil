import pytest
from pyutil import some


def test_some_with_empty_list():
    actual = some([], bool)
    expected = False
    assert actual == expected


def test_some_with_empty_tuple():
    actual = some((), bool)
    expected = False
    assert actual == expected


def test_some_with_empty_set():
    actual = some(set([]), bool)
    expected = False
    assert actual == expected


def test_some_when_func_returns_true():
    actual = some([1, 2, 3], lambda x: x > 0)
    expected = True
    assert actual == expected


def test_some_when_func_returns_true_2():
    actual = some([-12, -2, 0, 3], lambda x: x > 0)
    expected = True
    assert actual == expected


def test_some_when_func_returns_true_3():
    actual = some(["123", None, "false", False, ""], bool)
    expected = True
    assert actual == expected


def test_some_when_func_returns_false():
    actual = some([1, 2, 3, 4, 5], lambda x: x < 0)
    expected = False
    assert actual == expected


def test_some_when_func_returns_false_2():
    actual = some(["123", "abc", "foobar"], lambda x: len(x) > 10)
    expected = False
    assert actual == expected


def test_some_when_func_returns_false_3():
    actual = some([False, None, 0, ""], bool)
    expected = False
    assert actual == expected


def test_some_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        some("foo", bool)


def test_some_when_func_is_not_callable():
    with pytest.raises(TypeError):
        some([], "123")
