import argparse
import logging

from src.client import CoinGeckoClient
from src.processor import PriceProcessor
from src.reporter import ReportWriter

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def main():
    parser = argparse.ArgumentParser(description="Crypto price automation")
    parser.add_argument("--coin", default="bitcoin", help="Coin ID (eg. bitcoin)")
    parser.add_argument("--currency", default="usd", help="Currency (eg. usd)")
    parser.add_argument("--output", default="reports", help="Output directory")

    args = parser.parse_args()

    logging.info("Starting price fetch")
    
    client = CoinGeckoClient()
    processor = PriceProcessor()
    reporter = ReportWriter(args.output)

    raw_data = client.get_price(args.coin, args.currency)
    df = processor.normalize(raw_data)

    csv_path = reporter.to_csv(df)
    json_path = reporter.to_json(df)

    logging.info("CSV saved to %s", csv_path)
    logging.info("JSON saved to %s", json_path)
    

if __name__ == "__main__":
    main()
