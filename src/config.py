from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Directories
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
DATABASE_DIR = BASE_DIR / "database"

# Files
REQUIREMENTS_FILE = DATA_DIR / "requirements.json"
DATABASE_FILE = DATABASE_DIR / "testcases.db"
ANALYSIS_REPORT_FILE = OUTPUT_DIR / "analysis_report.md"
TEST_CASES_JSON = OUTPUT_DIR / "test_cases.json"
TEST_CASES_EXCEL = OUTPUT_DIR / "test_cases.xlsx"
COVERAGE_REPORT_FILE = OUTPUT_DIR / "coverage_report.md"

# Create required directories
OUTPUT_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)