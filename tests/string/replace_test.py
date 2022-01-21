import pytest
from pyutil import replace


def test_replace_with_empty_string():
    actual = replace("", "foo", "bar")
    expected = ""
    assert actual == expected


def test_replace_with_empty_target_string():
    actual = replace("foobar", "", "bar")
    expected = "foobar"
    assert actual == expected


def test_replace_with_empty_replacement_string():
    actual = replace("foo", "foo", "")
    expected = ""
    assert actual == expected


def test_replace_with_string():
    actual = replace("foobar", "bar", "foo")
    expected = "foofoo"
    assert actual == expected


def test_replace_with_string_2():
    actual = replace("foobarfoobar", "bar", "abc")
    expected = "fooabcfooabc"
    assert actual == expected


def test_replace_with_string_3():
    actual = replace("foobar", "foobar", "foo")
    expected = "foo"
    assert actual == expected


def test_replace_with_count():
    actual = replace("foobar", "bar", "foo", 1)
    expected = "foofoo"
    assert actual == expected


def test_replace_with_count_2():
    actual = replace("foobar", "bar", "foo", 0)
    expected = "foobar"
    assert actual == expected


def test_replace_with_count_3():
    actual = replace("foobarfoobar", "bar", "foo", 1)
    expected = "foofoofoobar"
    assert actual == expected


def test_replace_with_count_4():
    actual = replace("abcabcabcabcabc", "abc", "x", 3)
    expected = "xxxabcabc"
    assert actual == expected


def test_replace_with_count_4():
    actual = replace("abcabcabcabcabc", "abc", "x", 10)
    expected = "xxxxx"
    assert actual == expected


def test_replace_when_string_is_not_string():
    with pytest.raises(TypeError):
        replace(123, "foo", "bar")


def test_replace_when_target_is_not_string():
    with pytest.raises(TypeError):
        replace("foo", 123, "bar")


def test_replace_when_replacement_is_not_string():
    with pytest.raises(TypeError):
        replace("foo", "foo", 123)


def test_replace_when_n_is_not_integer():
    with pytest.raises(TypeError):
        replace("foo", "bar", "foo", "bar")


def test_replace_when_n_is_negative():
    with pytest.raises(ValueError):
        replace("foo", "bar", "foo", -3)
