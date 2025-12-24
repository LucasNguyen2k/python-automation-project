import pandas as pd
from src.reporter import ReportWriter

def test_report_writer(tmp_path):
    df = pd.DataFrame([
        { "coin": "bitcoin", "currency": "usd", "price": "50000"}
    ])

    writer = ReportWriter(tmp_path)
    csv_path = writer.to_csv(df)
    json_path = writer.to_json(df)

    assert csv_path.exists()
    assert json_path.exists()
