from datetime import datetime, date
from sqlalchemy import create_engine
import sys

from db.sqlite import SQLite
from etl.open_exchange.open_exchange_pipeline import OpenExchangePipeline
from etl.data_pipeline import PipelineManager
from utils.date_helpers import DateHelpers

engine = create_engine("sqlite:///exchanges.sqlite:", echo=True, future=True)
worker = SQLite(engine)

if len(sys.argv) == 1:
    start_date = date.today()
    print(start_date)

    pipeline = OpenExchangePipeline(start_date=start_date)
    manager = PipelineManager(pipeline, worker)
    manager.execute()

elif len(sys.argv) == 3:
    start_date = DateHelpers.str_to_date(sys.argv[1])
    end_date = DateHelpers.str_to_date(sys.argv[2])

    pipeline = OpenExchangePipeline(start_date=start_date, end_date=end_date)
    manager = PipelineManager(pipeline, worker)
    manager.execute()
