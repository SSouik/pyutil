from html import entities
import pytest
from pyutil import entries


def test_entries_when_dict_is_empty():
    actual = list(entries({}))
    expected = []
    assert actual == expected


def test_entries_when_dict_has_entires():
    actual = list(entries({"a": 1}))
    expected = [("a", 1)]
    assert actual == expected


def test_entries_when_dict_has_entires_2():
    actual = list(entries({"a": 1, "b": 2}))
    expected = [("a", 1), ("b", 2)]
    assert actual == expected


def test_entries_when_dict_has_entires_3():
    actual = list(entries({"a": 1, "foo": "bar"}))
    expected = [("a", 1), ("foo", "bar")]
    assert actual == expected


def test_entries_when_dict_has_entires_4():
    actual = list(entries({"a": 1, "key": "value", "key2": 123}))
    expected = [("a", 1), ("key", "value"), ("key2", 123)]
    assert actual == expected


def test_entries_when_dct_is_not_a_dict():
    with pytest.raises(TypeError):
        list(entries("foo"))
