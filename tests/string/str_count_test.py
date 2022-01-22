import pytest
from pyutil import str_count


def test_str_count_with_empty_string():
    actual = str_count("", "foo")
    expected = 0
    assert actual == expected


def test_str_count_with_empty_string_2():
    actual = str_count("", "foo", 2, 7)
    expected = 0
    assert actual == expected


def test_str_count_with_empty_target_string():
    actual = str_count("foo", "")
    expected = 0
    assert actual == expected


def test_str_count_with_empty_target_string_2():
    actual = str_count("foo", "", 3)
    expected = 0
    assert actual == expected


def test_str_count_with_empty_target_string_3():
    actual = str_count("foo", "", 1, 5)
    expected = 0
    assert actual == expected


def test_str_count_when_target_string_is_in_string():
    actual = str_count("foobar", "foo")
    expected = 1
    assert actual == expected


def test_str_count_when_target_string_is_in_string_2():
    actual = str_count("abcabcabc", "ab")
    expected = 3
    assert actual == expected


def test_str_count_when_target_string_is_in_string_3():
    actual = str_count("foobar", "foo", 2)
    expected = 0
    assert actual == expected


def test_str_count_when_target_string_is_in_string_4():
    actual = str_count("foobar", "foo", 0, 4)
    expected = 1
    assert actual == expected


def test_str_count_when_target_string_is_in_string_5():
    actual = str_count("foobar", "bar", 1, 10)
    expected = 1
    assert actual == expected


def test_str_count_when_target_string_is_in_string_6():
    actual = str_count("foobar", "o")
    expected = 2
    assert actual == expected


def test_str_count_when_start_and_end_index_are_equal():
    actual = str_count("foo", "bar", 1, 1)
    expected = 0
    assert actual == expected


def test_str_count_when_string_is_not_a_string():
    with pytest.raises(TypeError):
        str_count(123, "foo")


def test_str_count_when_target_is_not_a_string():
    with pytest.raises(TypeError):
        str_count("foo", 123)


def test_str_count_when_start_is_negative():
    with pytest.raises(ValueError):
        str_count("foo", "foo", -2)


def test_str_count_when_end_is_negative():
    with pytest.raises(ValueError):
        str_count("foo", "foo", 0, -3)


def test_str_count_when_start_is_greater_than_end():
    with pytest.raises(ValueError):
        str_count("foo", "foo", 10, 3)
