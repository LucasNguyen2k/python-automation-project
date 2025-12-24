from pathlib import Path
import pandas as pd

class ReportWriter:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def to_csv(self, df: pd.DataFrame, filename: str = "prices.csv") -> Path:
        path = self.output_dir / filename
        df.to_csv(path, index=False)
        return path

    def to_json(self, df: pd.DataFrame, filename: str="prices.json") -> Path:
        path = self.output_dir / filename
        df.to_json(path, orient="records", indent=2)
        return path
