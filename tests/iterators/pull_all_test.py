import pytest
from pyutil import pull_all


def test_pull_all_with_empty_list():
    lst = []
    pull_all(lst, [1])
    expected = []
    assert lst == expected


def test_pull_all_when_list_has_values():
    lst = [1, 2, 3, 4, 5]
    pull_all(lst, [2])
    expected = [1, 3, 4, 5]
    assert lst == expected


def test_pull_all_when_list_has_values_2():
    lst = [1, 2, 3, 4, 5]
    pull_all(lst, [2, 3, 4])
    expected = [1, 5]
    assert lst == expected


def test_pull_all_when_list_has_values_3():
    lst = [1, 2, 3, 4, 5]
    pull_all(lst, [1, 4])
    expected = [2, 3, 5]
    assert lst == expected


def test_pull_all_when_list_has_values_4():
    lst = [{"foo": 1, "bar": 2}, {"abc": 1, "def": 2}]
    pull_all(lst, [{"foo": 1, "bar": 2}])
    expected = [{"abc": 1, "def": 2}]
    assert lst == expected


def test_pull_all_when_list_has_duplicate_values():
    lst = [1, 2, 2, 3, 4, 4, 5]
    pull_all(lst, [2])
    expected = [1, 3, 4, 4, 5]
    assert lst == expected


def test_pull_all_when_list_has_duplicate_values_2():
    lst = [1, 2, 2, 3, 4, 4, 5]
    pull_all(lst, [2, 3, 4])
    expected = [1, 5]
    assert lst == expected


def test_pull_all_when_list_has_duplicate_values_3():
    lst = [1, 2, 2, 3, 4, 4, 5]
    pull_all(lst, [2, 4])
    expected = [1, 3, 5]
    assert lst == expected


def test_pull_all_seq_is_not_a_list():
    with pytest.raises(TypeError):
        pull_all("foo", 1)


def test_pull_all_all_when_pull_vals_is_not_valid():
    with pytest.raises(TypeError):
        pull_all([], 1)
