from openpyxl import Workbook


def export_to_excel(test_cases, file_path):

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Test Cases"

    sheet.append([
        "ID",
        "Type",
        "Description",
        "Expected Result"
    ])

    for tc in test_cases:
        sheet.append([
            tc.tc_id,
            tc.tc_type,
            tc.description,
            tc.expected_result
        ])

    workbook.save(file_path)