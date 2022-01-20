import pytest
from pyutil import remove_all_at


def test_remove_all_at_with_empty_list():
    actual = list(remove_all_at([], [1]))
    expected = []
    assert actual == expected


def test_remove_all_at_when_list_has_values():
    actual = list(remove_all_at([1, 2, 3, 4, 5], [2]))
    expected = [1, 2, 4, 5]
    assert actual == expected


def test_remove_all_at_when_list_has_values_2():
    actual = list(remove_all_at([1, 2, 3, 4, 5], (2, 3, 4)))
    expected = [1, 2]
    assert actual == expected


def test_remove_all_at_when_list_has_values_3():
    actual = list(remove_all_at([1, 2, 3, 4, 5], {1, 4}))
    expected = [1, 3, 4]
    assert actual == expected


def test_remove_all_at_when_list_has_values_4():
    actual = list(remove_all_at([{"foo": 1, "bar": 2}, {"abc": 1, "def": 2}], [0]))
    expected = [{"abc": 1, "def": 2}]
    assert actual == expected


def test_remove_all_at_when_list_has_values_5():
    actual = list(remove_all_at([1, 2, 3, 4, 5], (4, 1)))
    expected = [1, 3, 4]
    assert actual == expected


def test_remove_all_at_when_index_is_out_of_range():
    actual = list(remove_all_at([1, 2, 3], {10}))
    expected = [1, 2, 3]
    assert actual == expected


def test_remove_all_at_when_index_is_negative():
    with pytest.raises(ValueError):
        list(remove_all_at([], [-1]))


def test_remove_all_at_when_index_is_negative_2():
    with pytest.raises(ValueError):
        list(remove_all_at([], [1, -2]))


def test_remove_all_at_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(remove_all_at("foo", [1]))


def test_remove_all_at_when_remove_indices_is_not_valid():
    with pytest.raises(TypeError):
        list(remove_all_at([1, 2, 3], 1))


def test_remove_all_at_when_remove_indices_are_not_valid():
    with pytest.raises(ValueError):
        list(remove_all_at([], ["foo"]))


def test_remove_all_at_when_remove_indices_are_not_valid_2():
    with pytest.raises(ValueError):
        list(remove_all_at([], [1, "foo"]))


def test_remove_all_at_when_remove_indices_are_not_valid_2():
    with pytest.raises(ValueError):
        list(remove_all_at([], [-1, 10]))
