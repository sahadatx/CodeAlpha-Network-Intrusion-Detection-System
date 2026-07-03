from pathlib import Path

def test_log_exists():
    assert Path("logs/alerts.log").exists()

def test_reports_folder_exists():
    assert Path("reports").exists()

def test_script_exists():
    assert Path("scripts/analyze_logs.py").exists()
