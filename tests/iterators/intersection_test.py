import pytest
from pyutil import intersection


def test_intersection_with_empty_list():
    actual = list(intersection([]))
    expected = []
    assert actual == expected


def test_intersection_with_empty_tuple():
    actual = list(intersection(()))
    expected = []
    assert actual == expected


def test_intersection_with_one_param():
    actual = list(intersection([1, 2, 3]))
    expected = []
    assert actual == expected


def test_intersection_when_there_are_no_matching_values():
    actual = list(intersection([1, 2, 3], [4, 5, 6]))
    expected = []
    assert actual == expected


def test_intersection_when_there_are_matching_values_2():
    actual = list(intersection([1, 2, 3], (2, 3, 4, 5), [3, 4, 5]))
    expected = [3]
    assert actual == expected


def test_intersection_when_there_are_matching_values_3():
    actual = list(
        intersection(
            ("a", "b", "c", "d", "e"),
            [1, 2, "a", "b", "c"],
            (1, 3, 4, 5, "a", "c", "e"),
        )
    )
    expected = ["a", "c"]
    assert actual == expected


def test_intersection_when_there_are_matching_values_4():
    actual = list(intersection([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3]))
    expected = [1, 2, 3]
    assert actual == expected


def test_intersection_when_seqs_are_not_valid():
    with pytest.raises(TypeError):
        list(intersection([], "foo"))


def test_intersection_when_seqs_are_not_valid_2():
    with pytest.raises(TypeError):
        list(intersection(123, [], (1, 2, 3)))


def test_intersection_when_seqs_are_not_valid_3():
    with pytest.raises(TypeError):
        list(intersection([1, 2, 3], (), [], (), "foo"))
