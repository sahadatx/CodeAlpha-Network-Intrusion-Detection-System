import subprocess
import sys

def test_analyzer_runs():
    result = subprocess.run(
        [sys.executable, "scripts/analyze_logs.py"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    # Accept either a successful analysis or a clear missing-log message
    assert (
        "Total Alerts" in result.stdout
        or "[ERROR] alerts.log not found!" in result.stdout
    )