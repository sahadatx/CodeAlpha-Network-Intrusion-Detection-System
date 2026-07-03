from pathlib import Path

def test_txt_report():
    assert Path("reports/report.txt").exists()

def test_csv_report():
    assert Path("reports/report.csv").exists()

def test_json_report():
    assert Path("reports/report.json").exists()
