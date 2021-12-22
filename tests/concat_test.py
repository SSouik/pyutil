from pyutil.concat import concat


def test_concat_with_empty_list():
    actual = list(concat([]))
    expected = []
    assert actual == expected


def test_concat_with_empty_dict():
    actual = list(concat({}))
    expected = []
    assert actual == expected


def test_concat_with_empty_tuple():
    actual = list(concat(()))
    expected = []
    assert actual == expected


def test_concat_with_empty_string():
    actual = list(concat(""))
    expected = []
    assert actual == expected


def test_concat_with_numbers():
    actual = list(concat(1, 2, 3))
    expected = [1, 2, 3]
    assert actual == expected


def test_concat_with_numbers_and_list():
    actual = list(concat(1, 2, 3, [4, 5]))
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_concat_with_numbers_and_2D_list():
    actual = list(concat(1, 2, 3, [[4, 5], [6, 7]]))
    expected = [1, 2, 3, [4, 5], [6, 7]]
    assert actual == expected
