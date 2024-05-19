import unittest
from datetime import datetime, timedelta
from utils.date_helpers import DateHelpers  # replace 'your_module' with the actual name of your module file

class TestDateHelpers(unittest.TestCase):

    def test_str_to_date(self):
        date_str = "2024-05-19"
        expected_date = datetime(2024, 5, 19)
        self.assertEqual(DateHelpers.str_to_date(date_str), expected_date)

    def test_date_to_str(self):
        date = datetime(2024, 5, 19)
        expected_date_str = "2024-05-19"
        self.assertEqual(DateHelpers.date_to_str(date), expected_date_str)

    def test_daterange(self):
        start_date = datetime(2024, 5, 1)
        end_date = datetime(2024, 5, 4)
        expected_dates = [
            datetime(2024, 5, 1),
            datetime(2024, 5, 2),
            datetime(2024, 5, 3),
        ]
        self.assertEqual(list(DateHelpers.daterange(start_date, end_date)), expected_dates)

    def test_timestamp_to_date(self):
        timestamp = 1716096000  # corresponds to 2024-05-19
        expected_date = datetime(2024, 5, 19).date()
        self.assertEqual(DateHelpers.timestamp_to_date(timestamp), expected_date)
