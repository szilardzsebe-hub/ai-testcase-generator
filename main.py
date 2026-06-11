import json
from generator import generate_test_cases
from excel_exporter import export_to_excel


requirement = input("Enter requirement: ")

test_cases = generate_test_cases(requirement)

for tc in test_cases:
    print()
    print(f"ID: {tc.tc_id}")
    print(f"Type: {tc.tc_type}")
    print(f"Description: {tc.description}")
    print(f"Expected Result: {tc.expected_result}")

output = [tc.to_dict() for tc in test_cases]

json_path = "C:\\Users\\Szilard\\Documents\\AI_Assisted_Test_Case_Generator\\test_cases.json"
with open(json_path, "w") as file:
    json.dump(output, file, indent=4)

excel_path = "C:\\Users\\Szilard\\Documents\\AI_Assisted_Test_Case_Generator\\test_cases.xlsx"
export_to_excel(test_cases, excel_path)

print(f"\nTest cases saved to:")
print(f"  - JSON: {json_path}")
print(f"  - Excel: {excel_path}")