
import json
from excel_exporter import export_to_excel
from tc_id_service import init_db, get_or_generate_test_cases
from requirement_analyzer import analyze_requirement
from analysis_report import create_analysis_report
from coverage_report import create_coverage_report

from templates.login_test_data import LOGIN_TEST_DATA

print(LOGIN_TEST_DATA)

from analysis_report import (
    initialize_analysis_report,
    create_analysis_report
)
from config import (
    REQUIREMENTS_FILE,
    TEST_CASES_JSON,
    TEST_CASES_EXCEL,
)



init_db()

initialize_analysis_report()




with open(REQUIREMENTS_FILE, "r", encoding="utf-8") as file:
    requirements = json.load(file)


all_test_cases = []
analyses = []

for index, requirement in enumerate(requirements, start=1):

    analysis = analyze_requirement(requirement)
    analyses.append(analysis)
    create_analysis_report(requirement, analysis,index)
    test_cases = get_or_generate_test_cases(requirement)
    all_test_cases.extend(test_cases)
    


for tc in all_test_cases:
    print()
    print(f"ID: {tc.tc_id}")
    print(f"Type: {tc.tc_type}")
    print(f"Description: {tc.title}")
    print(f"Expected Result: {tc.expected_result}")


output = [tc.to_dict() for tc in all_test_cases]


with open(TEST_CASES_JSON, "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4)
   
print(f"Total test cases generated: {len(all_test_cases)}")
print(f"\nTest cases saved to:")
print(f"  - JSON: {TEST_CASES_JSON}")
print(f"  - Excel: {TEST_CASES_EXCEL}")

create_coverage_report(
    requirements,
    analyses,
    all_test_cases
)
export_to_excel(all_test_cases, TEST_CASES_EXCEL)