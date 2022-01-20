import pytest
from pyutil import pull_all_at


def test_pull_all_at_with_empty_list():
    lst = []
    pull_all_at(lst, [1])
    expected = []
    assert lst == expected


def test_pull_all_at_when_list_has_values():
    lst = [1, 2, 3, 4, 5]
    pull_all_at(lst, [2])
    expected = [1, 2, 4, 5]
    assert lst == expected


def test_pull_all_at_when_list_has_values_2():
    lst = [1, 2, 3, 4, 5]
    pull_all_at(lst, [2, 3, 4])
    expected = [1, 2]
    assert lst == expected


def test_pull_all_at_when_list_has_values_3():
    lst = [1, 2, 3, 4, 5]
    pull_all_at(lst, [1, 4])
    expected = [1, 3, 4]
    assert lst == expected


def test_pull_all_at_when_list_has_values_4():
    lst = [{"foo": 1, "bar": 2}, {"abc": 1, "def": 2}]
    pull_all_at(lst, [0])
    expected = [{"abc": 1, "def": 2}]
    assert lst == expected


def test_pull_all_at_when_list_has_values_5():
    lst = [1, 2, 3, 4, 5]
    pull_all_at(lst, [4, 1])
    expected = [1, 3, 4]
    assert lst == expected


def test_pull_all_at_when_index_is_out_of_range():
    lst = [1, 2, 3]
    pull_all_at(lst, [10])
    expected = [1, 2, 3]
    assert lst == expected


def test_pull_all_at_when_index_is_negative():
    with pytest.raises(ValueError):
        pull_all_at([], [-1])


def test_pull_all_at_when_index_is_negative_2():
    with pytest.raises(ValueError):
        pull_all_at([], [1, -2])


def test_pull_all_at_seq_is_not_a_list():
    with pytest.raises(TypeError):
        pull_all_at("foo", [1])


def test_pull_all_at_all_when_pull_indices_is_not_valid():
    with pytest.raises(ValueError):
        pull_all_at([], ["foo"])


def test_pull_all_at_all_when_pull_indices_is_not_valid_2():
    with pytest.raises(TypeError):
        pull_all_at([], "foo")


def test_pull_all_at_all_when_pull_vals_is_not_valid_2():
    with pytest.raises(ValueError):
        pull_all_at([], [1, "foo"])
