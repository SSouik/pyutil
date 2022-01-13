import pytest
from pyutil import join


def test_join_with_empty_list():
    actual = join([])
    expected = ""
    assert actual == expected


def test_join_with_empty_tuple():
    actual = join(())
    expected = ""
    assert actual == expected


def test_join_with_list():
    actual = join(["a", "b", "c", "d", "e"])
    expected = "a,b,c,d,e"
    assert actual == expected


def test_join_with_tuple():
    actual = join(("a", "b", "c", "d", "e"))
    expected = "a,b,c,d,e"
    assert actual == expected


def test_join_with_separator():
    actual = join(["a", "b", "c", "d", "e"], "-")
    expected = "a-b-c-d-e"
    assert actual == expected


def test_join_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        join("foo")


def test_join_when_separtor_is_not_valid():
    with pytest.raises(TypeError):
        join([], 123)
