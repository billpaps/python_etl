from datetime import datetime, timedelta

class DateHelpers:

    @staticmethod
    def str_to_date(date):
        return datetime.strptime(date, "%Y-%m-%d")
    
    @staticmethod
    def date_to_str(date):
        return datetime.strftime(date, "%Y-%m-%d")

    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    @staticmethod
    def timestamp_to_date(timestamp):
        return datetime.fromtimestamp(timestamp).date()
