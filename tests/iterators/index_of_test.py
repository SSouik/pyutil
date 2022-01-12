import pytest
from pyutil import index_of

sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_index_of_when_seq_is_empty_list():
    actual = index_of([], "foo")
    expected = -1
    assert actual == expected


def test_index_of_when_seq_is_empty_tuple():
    actual = index_of(tuple([]), "foo")
    expected = -1
    assert actual == expected


def test_index_of_when_seq_is_empty_string():
    actual = index_of("", "foo")
    expected = -1
    assert actual == expected


def test_index_of_with_list():
    actual = index_of(sample_data, 3)
    expected = 2
    assert actual == expected


def test_index_of_with_tuple():
    actual = index_of(tuple(sample_data), 3)
    expected = 2
    assert actual == expected


def test_index_of_with_string():
    actual = index_of("foobar", "b")
    expected = 3
    assert actual == expected


def test_index_of_with_list_with_from_index():
    actual = index_of(sample_data, 3, 1)
    expected = 2
    assert actual == expected


def test_index_of_with_tuple_from_index():
    actual = index_of(tuple(sample_data), 3, 1)
    expected = 2
    assert actual == expected


def test_index_of_with_string_from_index():
    actual = index_of("foobar", "b", 1)
    expected = 3
    assert actual == expected


def test_index_of_with_list_with_from_index_not_found():
    actual = index_of(sample_data, 3, 3)
    expected = -1
    assert actual == expected


def test_index_of_with_tuple_from_index_not_found():
    actual = index_of(tuple(sample_data), 3, 3)
    expected = -1
    assert actual == expected


def test_index_of_with_string_from_index_not_found():
    actual = index_of("foobar", "b", 4)
    expected = -1
    assert actual == expected


def test_index_of_with_list_with_from_index_is_negative():
    actual = index_of(sample_data, 3, -2)
    expected = 2
    assert actual == expected


def test_index_of_with_tuple_from_index_is_negative():
    actual = index_of(tuple(sample_data), 3, -2)
    expected = 2
    assert actual == expected


def test_index_of_with_string_from_index_is_negative():
    actual = index_of("foobar", "b", -2)
    expected = 3
    assert actual == expected


def test_index_of_with_list_with_from_index_is_negative_not_found():
    actual = index_of(sample_data, 3, -8)
    expected = -1
    assert actual == expected


def test_index_of_with_tuple_from_index_is_negative_not_found():
    actual = index_of(tuple(sample_data), 3, -8)
    expected = -1
    assert actual == expected


def test_index_of_with_string_from_index_is_negative_not_found():
    actual = index_of("foobar", "b", -4)
    expected = -1
    assert actual == expected


def test_index_of_when_from_index_is_out_of_range():
    actual = index_of(sample_data, 12)
    expected = -1
    assert actual == expected


def test_index_of_when_from_index_is_out_of_range_and_negative():
    actual = index_of(sample_data, -12)
    expected = -1
    assert actual == expected


def test_index_of_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        index_of(123, 123)
