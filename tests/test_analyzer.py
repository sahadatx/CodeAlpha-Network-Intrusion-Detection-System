import sys
import subprocess

def test_analyzer_runs():
    result = subprocess.run(
        [sys.executable, "scripts/analyze_logs.py"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Total Alerts" in result.stdout
