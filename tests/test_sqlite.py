import unittest
from datetime import date
from unittest.mock import patch, Mock, call
from sqlalchemy import create_engine

from db.sqlite import SQLite
from schemas.currency import Currency

class TestSQLite(unittest.TestCase):

    @patch('db.sqlite.Session')
    def test_save(self, mock_session):
        record = Currency(currency_symbol='AED', currency_date=date(2024, 5, 14), currency_rate=4.036203296703296)

        engine = create_engine("sqlite:///test.sqlite:", echo=True, future=True)
        db = SQLite(engine=engine)
        db.save([record])
