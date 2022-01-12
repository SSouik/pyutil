import pytest
from pyutil import groupby

number_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sample_data = [
    {"name": "Sam", "gender": "male"},
    {"name": "John", "gender": "male"},
    {"name": "Jane", "gender": "female"},
    {"name": "Chase", "gender": "male"},
    {"name": "Melanie", "gender": "female"},
]


def test_groupby_when_seq_is_empty_list():
    actual = groupby([], "foo")
    expected = {}
    assert actual == expected


def test_groupby_when_seq_is_empty_tuple():
    actual = groupby(tuple([]), "foo")
    expected = {}
    assert actual == expected


def test_groupby_when_seq_is_empty_set():
    actual = groupby(set([]), "foo")
    expected = {}
    assert actual == expected


def test_groupby_when_key_is_dict_key():
    actual = groupby(sample_data, "gender")
    expected = {
        "male": [
            {"name": "Sam", "gender": "male"},
            {"name": "John", "gender": "male"},
            {"name": "Chase", "gender": "male"},
        ],
        "female": [
            {"name": "Jane", "gender": "female"},
            {"name": "Melanie", "gender": "female"},
        ],
    }
    assert actual == expected


def test_groupby_when_key_is_callable():
    def even_odd(x):
        if x % 2 == 0:
            return "even"
        return "odd"

    actual = groupby(number_seq, even_odd)
    expected = {"even": [2, 4, 6, 8], "odd": [1, 3, 5, 7, 9]}
    assert actual == expected


def test_groupby_when_seq_is_not_valid():
    with pytest.raises(TypeError):
        groupby("foo", "foo")
