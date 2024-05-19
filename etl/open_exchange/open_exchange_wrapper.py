import requests

class OpenExchangeWrapper:

    @staticmethod
    # Get OpenExchange historical data
    def import_historical_data(date):
        # This must be in env var
        app_key = "b95b8a2a95c6459fac19324564dbc0a7"
        endpoint = "https://openexchangerates.org/api/historical/" + date + ".json?app_id=" + app_key

        response = requests.get(endpoint)
        response.raise_for_status()

        return response.json()