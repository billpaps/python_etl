import unittest
from unittest.mock import patch, MagicMock
from datetime import date
from sqlalchemy import create_engine

from db.sqlite import SQLite
from etl.open_exchange.open_exchange_pipeline import OpenExchangePipeline
from etl.open_exchange.open_exchange_wrapper import OpenExchangeWrapper
from etl.data_pipeline import PipelineManager
from schemas.currency import Currency

class TestOpenExchangePipeline(unittest.TestCase):

    def test_init(self):
        start_date = date(2024, 5, 10)
        end_date = date(2024, 5, 12)
        pipeline = OpenExchangePipeline(start_date, end_date)
        self.assertEqual(pipeline.start_date, start_date)
        self.assertEqual(pipeline.end_date, end_date)

        pipeline_no_end = OpenExchangePipeline(start_date)
        self.assertEqual(pipeline_no_end.start_date, start_date)
        self.assertIsNone(pipeline_no_end.end_date)

    def test_extract(self):
        pipeline, raw_data = self.__extract_data()

        self.assertEqual(raw_data[0]['rates'], {'AED': 3.672945, 'AFN': 72.303439, "EUR": 0.91})
        self.assertEqual(raw_data[0]['base'], 'USD')

    def test_extract_with_end_date(self):
        start_date = date(2024, 5, 10)
        end_date = date(2024, 5, 12)
        pipeline, raw_data = self.__extract_data(start_date=start_date, end_date=end_date)

        self.assertEqual(raw_data[0]['rates'], {'AED': 3.672945, 'AFN': 72.303439, "EUR": 0.91})
        self.assertEqual(raw_data[0]['base'], 'USD')

    def test_transform(self):
        pipeline, raw_data = self.__extract_data()
        currencies = pipeline.transform(raw_data)

        currency_aed = Currency(currency_symbol='AED', currency_date=date(2024, 5, 14), currency_rate=4.036203296703296)

        self.assertEqual(currencies[0].currency_rate, currency_aed.currency_rate)
        self.assertEqual(currencies[0].currency_symbol, currency_aed.currency_symbol)
        self.assertEqual(currencies[0].currency_date, currency_aed.currency_date)

    # @patch('db.sqlite.Session')
    # def test_load(self):
    #     pipeline, raw_data = self.__extract_data()
    #     currencies = pipeline.transform(raw_data)
    #     engine = create_engine("sqlite:///exchanges.sqlite:", echo=True, future=True)
    #     worker = SQLite(engine)
    #     pipeline.load(currencies[:1], worker)

    @patch('db.sqlite.Session')
    def integration_test(self):
        start_date = date(2024, 5, 10)
        pipeline = OpenExchangePipeline(start_date=start_date)
        engine = create_engine("sqlite:///test.sqlite:", echo=True, future=True)
        worker = SQLite(engine)
        manager = PipelineManager(pipeline, worker)
        manager.execute()

    # ---- private functions ----
    def __extract_data(self, start_date=date.today(), end_date=None):
        start_date = start_date
        wrapper = OpenExchangeWrapper
        wrapper.import_historical_data = MagicMock(return_value= self.__mock_response())
        pipeline = OpenExchangePipeline(start_date, end_date)
        raw_data = pipeline.extract()

        return pipeline, raw_data

    def __mock_response(date):
        mock_data = {
                "disclaimer": "Usage subject to terms: https://openexchangerates.org/terms",
                "license": "https://openexchangerates.org/license",
                "timestamp": 1715695200,
                "base": "USD",
                "rates": {
                    "AED": 3.672945,
                    "AFN": 72.303439,
                    "EUR": 0.91
                }
            }
    
        return mock_data
    