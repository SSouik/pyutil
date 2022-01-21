import pytest
from pyutil import endswith


def test_endswith_when_string_is_empty():
    actual = endswith("", "foo")
    expected = False
    assert actual == expected


def test_endswith_when_target_is_empty():
    actual = endswith("foo", "")
    expected = False
    assert actual == expected


def test_endswith_when_string_ends_with_target():
    actual = endswith("foo", "foo")
    expected = True
    assert actual == expected


def test_endswith_when_string_ends_with_target_2():
    actual = endswith("foobar", "bar")
    expected = True
    assert actual == expected


def test_endswith_when_string_ends_with_target_3():
    actual = endswith("abc123", "3")
    expected = True
    assert actual == expected


def test_endswith_when_string_ends_with_target_4():
    actual = endswith("abc123", "123")
    expected = True
    assert actual == expected


def test_endswith_when_string_ends_with_target_5():
    actual = endswith("foobar", "foobar")
    expected = True
    assert actual == expected


def test_endswith_when_string_does_not_end_with_target():
    actual = endswith("foo", "123")
    expected = False
    assert actual == expected


def test_endswith_when_string_does_not_end_with_target_2():
    actual = endswith("foo", "f")
    expected = False
    assert actual == expected


def test_endswith_when_string_does_not_end_with_target_3():
    actual = endswith("foo", "fo")
    expected = False
    assert actual == expected


def test_endswith_when_string_does_not_end_with_target_4():
    actual = endswith("abc123", "13")
    expected = False
    assert actual == expected


def test_endswith_when_string_does_not_end_with_target_5():
    actual = endswith("abc123", "bar")
    expected = False
    assert actual == expected


def test_endswith_when_string_is_not_string():
    with pytest.raises(TypeError):
        endswith(123, "foo")


def test_endswith_when_target_is_not_string():
    with pytest.raises(TypeError):
        endswith("123", 123)
