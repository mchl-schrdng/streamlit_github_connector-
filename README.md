# Streamlit + CoinMarketCap Integration
<img src="./streamlit-logo.png" alt="Streamlit Logo" width="100"/> <img src="./cmc-logo.png" alt="CMC Logo" width="100"/>

This repository contains a Streamlit application that serves as a connector to the CoinMarketCap API, allowing users to fetch and explore cryptocurrency data with ease.

## 🚀 Features

- **Fetch Latest Cryptocurrencies**: Retrieve information about the top N cryptocurrencies sorted by market cap.
- **Search Cryptocurrencies**: Search for specific cryptocurrencies based on keywords.
- **Fetch Historical Data**: Obtain historical data for a specific cryptocurrency within a given date range.

## 📦 Package Dependencies

To run the Streamlit CoinMarketCap Connector, you'll need to install the following Python packages:

- `streamlit`: The primary framework used for building the web application.
- `requests`: Utilized for making API requests to CoinMarketCap.
- `polars`: An optional package if you decide to integrate it for data manipulation and visualization.

After cloning the repository, you can easily install these dependencies using the provided `requirements.txt` file.

## 🔥 Note

Certain functionalities, such as fetching historical data, might require a specific subscription plan on CoinMarketCap. If you encounter the following exception:

```
Exception: Error fetching data:
{
    "status": {
        "timestamp": "2023-07-27T20:27:50.369Z",
        "error_code": 1006,
        "error_message": "Your API Key subscription plan doesn't support this endpoint.",
        "elapsed": 0,
        "credit_count": 0
    }
}
```

It indicates that your current API subscription plan doesn't support the endpoint you're trying to access. Consider upgrading or modifying your plan on CoinMarketCap to access those specific features.
