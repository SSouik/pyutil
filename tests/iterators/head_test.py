from pyutil import head


def test_head_with_empty_list():
    actual = head([])
    expected = None
    assert actual == expected


def test_head_with_empty_tuple():
    actual = head(tuple([]))
    expected = None
    assert actual == expected


def test_head_with_empty_string():
    actual = head("")
    expected = None
    assert actual == expected


def test_head_with_list():
    actual = head([1, 2, 3, 4])
    expected = 1
    assert actual == expected


def test_head_with_tuple():
    actual = head((1, 2, 3, 4))
    expected = 1
    assert actual == expected


def test_head_with_string():
    actual = head("foo")
    expected = "f"
    assert actual == expected
