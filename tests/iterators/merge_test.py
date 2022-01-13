import pytest
from pyutil import merge


def test_merge_with_empty_list():
    actual = list(merge([]))
    expected = []
    assert actual == expected


def test_merge_with_empty_tuple():
    actual = list(merge(()))
    expected = []
    assert actual == expected


def test_merge_with_empty_set():
    actual = list(merge(set({})))
    expected = []
    assert actual == expected


def test_merge_with_empty_string():
    actual = list(merge(""))
    expected = []
    assert actual == expected


def test_merge_with_one_param():
    actual = list(merge([1, 2, 3]))
    expected = [1, 2, 3]
    assert actual == expected


def test_merge_with_multiple_seqs():
    actual = list(merge([1, 2, 3], (1, 2, 3, 4, 5, 6)))
    expected = [1, 2, 3, 4, 5, 6]
    assert actual == expected


def test_merge_with_multiple_seqs_2():
    actual = list(merge([1, 2, 3], (1, 2, "abc", "def", 3, 1, 2)))
    expected = [1, 2, 3, "abc", "def"]
    assert actual == expected


def test_merge_with_multiple_seqs_3():
    actual = list(merge("abc", "bca", "foo"))
    expected = ["a", "b", "c", "f", "o"]
    assert actual == expected


def test_merge_when_seqs_are_not_valid():
    with pytest.raises(TypeError):
        list(merge(123))


def test_merge_when_seqs_are_not_valid_2():
    with pytest.raises(TypeError):
        list(merge([], 123))


def test_merge_when_seqs_are_not_valid_3():
    with pytest.raises(TypeError):
        list(merge("foo", [], 123))
