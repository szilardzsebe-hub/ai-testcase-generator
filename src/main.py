
import json
from generator import generate_test_cases
from excel_exporter import export_to_excel
from tc_id_service import init_db
from pathlib import Path
from requirement_analyzer import analyze_requirement
from analysis_report import create_analysis_report




init_db()
BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
report = OUTPUT_DIR / "analysis_report.md"

if report.exists():
    report.unlink()

requirements_path = BASE_DIR / "data" / "requirements.json"

with open(requirements_path, "r", encoding="utf-8") as file:
    requirements = json.load(file)

all_test_cases = []

for requirement in requirements:

    analysis = analyze_requirement(requirement)
    create_analysis_report(requirement, analysis)

    from tc_id_service import get_or_generate_test_cases

    test_cases = get_or_generate_test_cases(requirement)
    all_test_cases.extend(test_cases)



for tc in all_test_cases:
    print()
    print(f"ID: {tc.tc_id}")
    print(f"Type: {tc.tc_type}")
    print(f"Description: {tc.description}")
    print(f"Expected Result: {tc.expected_result}")


output = [tc.to_dict() for tc in all_test_cases]

json_path = OUTPUT_DIR / "test_cases.json"
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4)

excel_path = OUTPUT_DIR / "test_cases.xlsx"
export_to_excel(all_test_cases, excel_path)

print(f"Total test cases generated: {len(all_test_cases)}")
print(f"\nTest cases saved to:")
print(f"  - JSON: {json_path}")
print(f"  - Excel: {excel_path}")