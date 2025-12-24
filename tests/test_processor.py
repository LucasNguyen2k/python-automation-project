import pytest
from src.processor import PriceProcessor

def test_invalid_price_data():
    processor = PriceProcessor()
    raw_data = {"bitcoin": {"usd": "invalid"}}

    with pytest.raises(ValueError):
        processor.normalize(raw_data)
        
