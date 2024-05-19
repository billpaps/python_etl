from datetime import datetime, timedelta

# Helper functions for datetimes
class DateHelpers:

    @staticmethod
    def str_to_date(date: str):
        return datetime.strptime(date, "%Y-%m-%d")
    
    @staticmethod
    def date_to_str(date: datetime):
        return datetime.strftime(date, "%Y-%m-%d")

    @staticmethod
    def daterange(start_date: datetime, end_date: datetime):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    @staticmethod
    def timestamp_to_date(timestamp: int):
        return datetime.fromtimestamp(timestamp).date()
