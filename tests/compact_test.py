import pytest
from pyutil import compact


def test_compact_with_false():
    lst = [1, 2, False]
    actual = list(compact(lst))
    expected = [1, 2]
    assert actual == expected


def test_compact_with_true():
    lst = [1, 2, True]
    actual = list(compact(lst))
    expected = [1, 2, True]
    assert actual == expected


def test_compact_with_empty_dict():
    lst = [1, 2, {}]
    actual = list(compact(lst))
    expected = [1, 2]
    assert actual == expected


def test_compact_with_dict():
    lst = [1, 2, {"a": 1}]
    actual = list(compact(lst))
    expected = [1, 2, {"a": 1}]
    assert actual == expected


def test_compact_with_None():
    lst = [1, 2, None]
    actual = list(compact(lst))
    expected = [1, 2]
    assert actual == expected


def test_compact_with_empty_string():
    lst = [1, 2, ""]
    actual = list(compact(lst))
    expected = [1, 2]
    assert actual == expected


def test_compact_with_empty_string():
    lst = [1, 2, "foo"]
    actual = list(compact(lst))
    expected = [1, 2, "foo"]
    assert actual == expected


def test_compact_with_zero():
    lst = [1, 2, 0]
    actual = list(compact(lst))
    expected = [1, 2]
    assert actual == expected


def test_compact_when_seq_is_empty():
    actual = list(compact([]))
    expected = []
    assert actual == expected


def test_compact_when_seq_is_tuple():
    tup = (1, 2, False)
    actual = list(compact(tup))
    expected = [1, 2]
    assert actual == expected


def test_compact_when_seq_is_set():
    set = {1, 2, False}
    actual = list(compact(set))
    expected = [1, 2]
    assert actual == expected


def test_compact_when_seq_is_tuple():
    tup = (1, 2, False)
    actual = list(compact(tup))
    expected = [1, 2]
    assert actual == expected


def test_compact_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(compact("foo"))
