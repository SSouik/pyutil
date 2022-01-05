import pytest
from pyutil import difference


def test_difference_when_list_is_empty():
    actual = list(difference([], [1, 2, 3]))
    expected = []
    assert actual == expected


def test_difference_when_tuple_is_empty():
    actual = list(difference((), [1, 2, 3]))
    expected = []
    assert actual == expected


def test_difference_when_set_is_empty():
    actual = list(difference(set([]), [1, 2, 3]))
    expected = []
    assert actual == expected


def test_difference_when_seq_is_list():
    actual = list(difference([1, 2, 3], [1, 2]))
    expected = [3]
    assert actual == expected


def test_difference_when_seq_is_tuple():
    actual = list(difference((1, 2, 3), [1, 2]))
    expected = [3]
    assert actual == expected


def test_difference_when_seq_is_set():
    actual = list(difference({1, 2, 3}, [1, 2]))
    expected = [3]
    assert actual == expected


def test_difference_when_exclude_value_is_a_dict():
    actual = list(difference([1, 2, 3], {"a": 1}))
    expected = [2, 3]
    assert actual == expected


def test_difference_when_seq_is_string():
    with pytest.raises(TypeError):
        list(difference("foo", [1, 2, 3]))


def test_difference_when_seq_is_int():
    with pytest.raises(TypeError):
        list(difference(1, [1, 2, 3]))


def test_difference_when_seq_is_dict():
    with pytest.raises(TypeError):
        list(difference({}, [1, 2, 3]))


def test_difference_when_exclude_value_is_not_a_seq():
    with pytest.raises(TypeError):
        list(difference([1, 2, 3], 1))
