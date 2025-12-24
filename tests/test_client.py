import pytest
import requests
from unittest.mock import patch

from src.client import CoinGeckoClient

@patch("src.client.requests.get")
def test_get_price_success(mock_get):
    mock_get.return_value.status_code=200
    mock_get.return_value.json.return_value = {
        "bitcoin": {"usd": 50000}
    }

    client = CoinGeckoClient()
    data = client.get_price("bitcoin", "usd")

    assert data["bitcoin"]["usd"] == 50000

@patch("src.client.requests.get")
def test_get_price_http_error(mock_get):
    mock_get.side_effect = requests.exceptions.HTTPError("API down")

    client = CoinGeckoClient()

    with pytest.raises(RuntimeError):
        client.get_price("bitcoin", "usd")
