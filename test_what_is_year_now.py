import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    @patch('what_is_year_now.urllib.request.urlopen')
    def test_ymd_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            '{"currentDateTime": "2023-01-01"}'
        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_dmy_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            '{"currentDateTime": "01.01.2001"}'
        year = what_is_year_now()
        self.assertEqual(year, 2001)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_invalid_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            '{"currentDateTime": "01/01/2020"}'
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
