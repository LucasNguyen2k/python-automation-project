import requests
from typing import Dict, Any

from src.config import settings

class CoinGeckoClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.timeout = settings.TIMEOUT

    def get_price(self, coin_id: str, currency: str = "usd")-> Dict[str, Any]:
        url = f"{self.base_url}/simple/price"
        params = {
            "ids": coin_id,
            "vs_currencies": currency
        }

        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise RuntimeError(f"API request failed: {exc}") from exc

        data = response.json()

        if coin_id not in data:
            raise ValueError(f"Coin '{coin_id}' not found in API response")

        return data
