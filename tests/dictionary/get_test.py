import pytest
from pyutil import get

sample_data = {"key": "foo", "key2": {"nestedKey": "bar", "nestedKey2": {"bar": 123}}}


def test_get_with_empty_dict():
    actual = get({}, "foo")
    expected = None
    assert actual == expected


def test_get_with_empty_dict_and_default_is_set():
    actual = get({}, "foo", "bar")
    expected = "bar"
    assert actual == expected


def test_get_with_empty_dict_and_nested_key_path():
    actual = get({}, "foo.bar")
    expected = None
    assert actual == expected


def test_get_with_empty_dict_and_and_nested_key_path_and_default_is_set():
    actual = get({}, "foo.bar", "bar")
    expected = "bar"
    assert actual == expected


def test_get_with_dict():
    actual = get(sample_data, "key")
    expected = "foo"
    assert actual == expected


def test_get_with_dict_2():
    actual = get(sample_data, "key", "bar")
    expected = "foo"
    assert actual == expected


def test_get_with_dict_3():
    actual = get(sample_data, "key2.nestedKey")
    expected = "bar"
    assert actual == expected


def test_get_with_dict_4():
    actual = get(sample_data, "key2.nestedKey", "abc123")
    expected = "bar"
    assert actual == expected


def test_get_with_dict_5():
    actual = get(sample_data, "key2", "abc123")
    expected = {"nestedKey": "bar", "nestedKey2": {"bar": 123}}
    assert actual == expected


def test_get_with_dict_6():
    actual = get(sample_data, "key2.nestedKey2.bar", "abc123")
    expected = 123
    assert actual == expected


def test_get_with_dict_7():
    actual = get(sample_data, "key2.nestedKey2", "abc123")
    expected = {"bar": 123}
    assert actual == expected


def test_get_when_key_does_not_exist():
    actual = get(sample_data, "foo")
    expected = None
    assert actual == expected


def test_get_when_key_does_not_exist_2():
    actual = get(sample_data, "foo", 123)
    expected = 123
    assert actual == expected


def test_get_when_key_does_not_exist_3():
    actual = get(sample_data, "key.foo")
    expected = None
    assert actual == expected


def test_get_when_key_does_not_exist_4():
    actual = get(sample_data, "key.foo", "foo")
    expected = "foo"
    assert actual == expected


def test_get_when_key_does_not_exist_5():
    actual = get(sample_data, "key.nestedKey.foo")
    expected = None
    assert actual == expected


def test_get_when_key_does_not_exist_6():
    actual = get(sample_data, "key.nestedKey2.bar.foo", "abc123")
    expected = "abc123"
    assert actual == expected


def test_get_when_dct_is_not_a_dict():
    with pytest.raises(TypeError):
        get("foo", "bar")


def test_get_when_key_path_is_not_a_string():
    with pytest.raises(TypeError):
        get({}, 123)
