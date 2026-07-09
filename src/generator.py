from models import TestCase
from requirement_analyzer import analyze_requirement
from risk_templates import RISK_TEMPLATES
from validation_templates import VALIDATION_TEMPLATES
from positive_templates import POSITIVE_TEMPLATES
from models import TestCase


def generate_positive_tests(analysis):

    if analysis.category not in POSITIVE_TEMPLATES:
        return []

    tc_type, description, expected = POSITIVE_TEMPLATES[analysis.category]

    return [
        TestCase(
            None,
            tc_type,
            description,
            expected
        )
    ]
def generate_risk_tests(analysis):

    tests = []

    for risk in analysis.risks:

        if risk in RISK_TEMPLATES:

            tc_type, description, expected = RISK_TEMPLATES[risk]

            tests.append(
                TestCase(
                    None,
                    tc_type,
                    description,
                    expected
                )
            )

    return tests
def generate_validation_tests(analysis):

    tests = []

    for validation in analysis.validations:

        if validation in VALIDATION_TEMPLATES:

            tc_type, description, expected = VALIDATION_TEMPLATES[validation]

            tests.append(
                TestCase(
                    None,
                    tc_type,
                    description,
                    expected
                )
            )

    return tests
def generate_boundary_tests(analysis):

    if analysis.category == "LOGIN":

        return [
            TestCase(
                None,
                "Boundary",
                "Verify login with maximum username length",
                "Request handled correctly"
            )
        ]

    return []

def generate_test_cases(requirement):

    analysis = analyze_requirement(requirement)

    test_cases = []

    test_cases.extend(generate_positive_tests(analysis))
    test_cases.extend(generate_risk_tests(analysis))
    test_cases.extend(generate_validation_tests(analysis))
    test_cases.extend(generate_boundary_tests(analysis))

    return test_cases
 