import pytest
from one_hot_encoder import fit_transform


def test_empty_input():
    with pytest.raises(TypeError):
        fit_transform()


def test_invalid_input():
    with pytest.raises(TypeError):
        fit_transform(0)


def test_artem_sukhov_me():
    result = fit_transform('artem', 'sukhov', 'me')
    expected = [
        ('artem', [0, 0, 1]),
        ('sukhov', [0, 1, 0]),
        ('me', [1, 0, 0])
    ]
    assert result == expected


def test_list_artem_sukhov_me():
    result = fit_transform(['artem', 'sukhov', 'me'])
    assert ('artem', [0, 0, 1]) in result


def test_artem_sukhov_artem():
    result = fit_transform('artem', 'sukhov', 'artem')
    expected = [
        ('artem', [0, 1]),
        ('sukhov', [1, 0]),
        ('artem', [0, 1])
    ]
    assert result == expected
