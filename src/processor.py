from typing import Dict, Any
import pandas as pd

class PriceProcessor:
    REQUIRED_FIELDS = ("coin", "currency", "price")

    def normalize(self, raw_data: Dict[str, Any]) -> pd.DataFrame:
        if not raw_data:
            raise ValueError("Raw data is empty")

        records = []

        for coin, prices in raw_data.items():
            if not isinstance(prices, dict):
                continue

        for currency, value in prices.items():
            if not isinstance(value, (int, float)):
                continue

            records.append({
                "coin": coin,
                "currency": currency,
                "price": value
            })

        if not records:
            raise ValueError("No valid price data found")

        df = pd.DataFrame(records)

        return df[list(self.REQUIRED_FIELDS)]
    
