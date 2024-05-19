from etl.open_exchange.open_exchange_wrapper import OpenExchangeWrapper
from utils.date_helpers import DateHelpers
from etl.data_pipeline import DataPipeline
from schemas.currency import Currency

class OpenExchangePipeline(DataPipeline):

    def __init__(self, start_date, end_date = None) -> None:
        super().__init__()
        self.start_date = start_date
        self.end_date = None if end_date==None else end_date

    def extract(self):
        raw_data = []
        if self.end_date is None:
            print(f"Extracting data for {self.start_date}")
            self.start_date = DateHelpers.date_to_str(self.start_date)
            raw_data.append(OpenExchangeWrapper.import_historical_data(self.start_date))
        else:            
            raw_data = []
            for single_date in DateHelpers.daterange(self.start_date, self.end_date):
                single_date = DateHelpers.date_to_str(single_date)
                print(f"Extracting data for {single_date}")
                raw_data.append(OpenExchangeWrapper.import_historical_data(single_date))

        return raw_data

    def transform(self, data):
        records = []
        for record in data:
            date = DateHelpers.timestamp_to_date(record['timestamp'])
            euro_rate = record['rates']['EUR']
            for symbol in record['rates'].keys():
                # print("For symbol: " + symbol + " the rate is: " + str(record['rates'][symbol]/euro_rate))
                curr = record['rates'][symbol] / euro_rate
                data_record = Currency(
                    currency_symbol = symbol,
                    currency_rate = curr,
                    currency_date = date
                )
                records.append(data_record)

        return records

    def load(self, data, worker):
        worker.save(data)