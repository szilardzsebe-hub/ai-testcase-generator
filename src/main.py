
import json

from src.analysis_report import (
    create_analysis_report,
    initialize_analysis_report,
)

from src.config import (
    REQUIREMENTS_FILE,
    TEST_CASES_EXCEL,
    TEST_CASES_JSON,
)
from src.coverage_report import create_coverage_report
from src.excel_exporter import export_to_excel
from src.requirement_analyzer import analyze_requirement
from src.tc_id_service import (
    get_or_generate_test_cases,
    init_db,
)


"""
    Application entry point.

    Loads requirements, generates test cases,
    creates reports and exports the results.
"""
def main():
         
    #Application entry point.
    #Loads requirements, generates test cases,
    #creates reports and exports the results.
    

    init_db()

    initialize_analysis_report()

    with open(REQUIREMENTS_FILE, "r", encoding="utf-8") as file:
        requirements = json.load(file)

    all_test_cases = []
    analyses = []

    for index, requirement in enumerate(requirements, start=1):

        analysis = analyze_requirement(requirement)
        analyses.append(analysis)
        create_analysis_report(requirement, analysis, index)
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

    create_coverage_report(requirements, analyses, all_test_cases)
    export_to_excel(all_test_cases, TEST_CASES_EXCEL)

if __name__ == "__main__":
    main()
    