import json
from generator import generate_test_cases
from excel_exporter import export_to_excel



with open("C:\\Users\\Szilard\\Documents\\AI_Assisted_Test_Case_Generator\\data\\requirements.json", "r") as file:
    requirements = json.load(file)

all_test_cases = []

for requirement in requirements:
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

json_path = "C:\\Users\\Szilard\\Documents\\AI_Assisted_Test_Case_Generator\\test_cases.json"
with open(json_path, "w") as file:
    json.dump(output, file, indent=4)

excel_path = "C:\\Users\\Szilard\\Documents\\AI_Assisted_Test_Case_Generator\\test_cases.xlsx"
export_to_excel(all_test_cases, excel_path)

print(f"Total test cases generated: {len(all_test_cases)}")
print(f"\nTest cases saved to:")
print(f"  - JSON: {json_path}")
print(f"  - Excel: {excel_path}")