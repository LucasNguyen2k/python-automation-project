from src.client import CoinGeckoClient
from src.processor import PriceProcessor

def main():
    client = CoinGeckoClient()
    processor = PriceProcessor()

    raw_data = client.get_price("bitcoin", "usd")
    df = processor.normalize(raw_data)
    
    print(df)

if __name__ == "__main__":
    main()
