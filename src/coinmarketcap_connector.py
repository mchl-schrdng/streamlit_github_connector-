from streamlit.connections import ExperimentalBaseConnection
import streamlit as st
import requests
import os
import time

class CoinMarketCapConnection(ExperimentalBaseConnection):
    BASE_URL = "https://pro-api.coinmarketcap.com/v1/"

    def __init__(self, connection_name):
        super().__init__(connection_name)
        self._connect()

    def _connect(self, **kwargs):
        # Fetch the API key from the environment
        self.api_key = st.secrets["coinmarketcap"]["api_key"]
        if not self.api_key:
            raise ValueError("CoinMarketCap API Key not found in environment!")

        self._rate_limit_reset = time.time() + 60  # Reset in 60 seconds by default
        self._rate_limit_remaining = 30  # Default to a reasonable number of requests

    def _get_headers(self):
        return {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key,
        }

    def _handle_rate_limit(self, response):
        self._rate_limit_remaining = int(response.headers.get("X-CMC_PRO_API_REQUESTS_REMAINING", 30))
        self._rate_limit_reset = time.time() + int(response.headers.get("X-CMC_PRO_API_REQUESTS_RESET_IN", 60))

        if self._rate_limit_remaining <= 0:
            sleep_time = self._rate_limit_reset - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

    def _request(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self._get_headers(), params=params)

        if "X-CMC_PRO_API_REQUESTS_REMAINING" in response.headers:
            self._handle_rate_limit(response)

        if response.status_code != 200:
            raise Exception(f"Error fetching data: {response.text}")

        return response.json()

    def fetch_latest_data(self, limit=100):
        return self._request("cryptocurrency/listings/latest", params={"limit": limit})

    def fetch_historical_data(self, cryptocurrency_id, start_date, end_date):
        params = {
            "id": cryptocurrency_id,
            "time_start": start_date,
            "time_end": end_date
        }
        return self._request("cryptocurrency/quotes/historical", params=params)
