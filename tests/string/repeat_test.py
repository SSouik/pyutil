import pytest
from pyutil import repeat


def test_repeat_with_empty_string():
    actual = repeat("", 1)
    expected = ""
    assert actual == expected


def test_repeat_with_string():
    actual = repeat("abc", 2)
    expected = "abcabc"
    assert actual == expected


def test_repeat_with_string_2():
    actual = repeat("123", 4)
    expected = "123123123123"
    assert actual == expected


def test_repeat_with_string_3():
    actual = repeat("foobar", 0)
    expected = ""
    assert actual == expected


def test_repeat_with_string_4():
    actual = repeat("x", 2)
    expected = "xx"
    assert actual == expected


def test_repeat_with_string_5():
    actual = repeat("foobar", 3)
    expected = "foobarfoobarfoobar"
    assert actual == expected


def test_repeat_when_string_is_not_string():
    with pytest.raises(TypeError):
        repeat(123, 1)


def test_repeat_when_n_is_not_integer():
    with pytest.raises(TypeError):
        repeat("foobar", "")


def test_repeat_when_n_is_negative():
    with pytest.raises(ValueError):
        repeat("foobar", -2)
