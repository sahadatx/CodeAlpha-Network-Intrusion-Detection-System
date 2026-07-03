from pathlib import Path

def test_reports_folder_exists():
    assert Path("reports").exists()

def test_script_exists():
    assert Path("scripts/analyze_logs.py").exists()

def test_rules_exist():
    assert Path("rules/local.rules").exists()