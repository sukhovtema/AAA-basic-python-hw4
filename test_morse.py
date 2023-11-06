import pytest
from morse import decode


@pytest.mark.parametrize('morse_input, expected_output', [
    ('... --- ...', 'SOS'),
    ('.- .-. - . -- .----', 'ARTEM1'),
    ('-... . . .-.', 'BEER'),
])
def test_decode(morse_input, expected_output):
    """Проверяем верные коды"""
    assert decode(morse_input) == expected_output


if __name__ == '__main__':
    pytest.main()
