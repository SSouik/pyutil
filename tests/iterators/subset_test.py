import pytest
from pyutil import subset

def test_subset_with_empty_list():
    actual = list(subset([]))
    expected = []
    assert actual == expected

def test_subset_with_empty_tuple():
    actual = list(subset(()))
    expected = []
    assert actual == expected

def test_subset_when_seq_has_values():
    actual = list(subset([1, 2, 3, 4, 5, 6], 1))
    expected = [2, 3, 4, 5, 6]
    assert actual == expected

def test_subset_when_seq_has_values_2():
    actual = list(subset([1, 2, 3, 4, 5, 6], 1, 4))
    expected = [2, 3, 4]
    assert actual == expected

def test_subset_when_seq_has_values_3():
    actual = list(subset((1, 2, 3, 4, 5, 6), 0, 2))
    expected = [1, 2]
    assert actual == expected

def test_subset_when_seq_has_values_4():
    actual = list(subset([1, 2, 3, 4, 5, 6], 1, 1))
    expected = []
    assert actual == expected

def test_subset_when_start_is_negative():
    with pytest.raises(ValueError):
        list(subset([], -1))

def test_subset_when_end_is_negative():
    with pytest.raises(ValueError):
        list(subset([], 0, -1))

def test_subset_when_start_is_greater_than_end_is_negative():
    with pytest.raises(ValueError):
        list(subset([], 3, 2))

def test_subset_when_start_is_greater_than_end_is_negative_2():
    with pytest.raises(ValueError):
        list(subset([], 3))

def test_subset_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        list(subset("abc"))
