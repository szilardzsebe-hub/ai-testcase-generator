from builder.testcase_builder import create_test_case
from templates.boundary_templates import BOUNDARY_TEMPLATES
from requirement_analyzer import analyze_requirement
from templates.risk_templates import RISK_TEMPLATES
from templates.validation_templates import VALIDATION_TEMPLATES
from templates.positive_templates import POSITIVE_TEMPLATES
from models import (
    TestType,
    Priority,
    
)

# Generates multiple test cases from a collection of reusable templates.
# Eliminates duplicated generation logic for Risk, Validation and similar
# test case categories.
def generate_from_template(
    analysis,
    template,
    items,
    priority,
    tag,
):

    tests = []

    for item in items:

        if item not in template:
            continue

        tc_type, description, expected = template[item]

        tests.append(
            create_test_case(
                analysis=analysis,
                title=description,
                tc_type=tc_type,
                priority=priority,
                expected_result=expected,
                tags=[tag],
            )
        )

    return tests
def generate_positive_tests(analysis):
    
    if analysis.category not in POSITIVE_TEMPLATES:
        return []
    
    tc_type,description, expected = POSITIVE_TEMPLATES[analysis.category]

    return [
        create_test_case(
            analysis=analysis,
            title=description,
            tc_type=tc_type,
            priority=Priority.MEDIUM,
            expected_result=expected,
            tags=["Positive"],
        )
    ]


def generate_risk_tests(analysis):

    return generate_from_template(
        analysis=analysis,
        template=RISK_TEMPLATES,
        items=analysis.risks,
        priority=Priority.HIGH,
        tag="Risk",
    )

    return tests
def generate_validation_tests(analysis):

    return generate_from_template(
        analysis=analysis,
        template=VALIDATION_TEMPLATES,
        items=analysis.validations,
        priority=Priority.MEDIUM,
        tag="Validation",
    )

def generate_boundary_tests(analysis):

    if analysis.category not in BOUNDARY_TEMPLATES:
        return []

    tc_type, description, expected = BOUNDARY_TEMPLATES[analysis.category]

    return [
        create_test_case(
            analysis=analysis,
            title=description,
            tc_type=tc_type,
            priority=Priority.MEDIUM,
            expected_result=expected,
            tags=["Boundary"],
        )
    ]

def generate_test_cases(requirement):

    analysis = analyze_requirement(requirement)

    test_cases = []

    test_cases.extend(generate_positive_tests(analysis))
    test_cases.extend(generate_risk_tests(analysis))
    test_cases.extend(generate_validation_tests(analysis))
    test_cases.extend(generate_boundary_tests(analysis))

    return test_cases
 
# Generates multiple test cases from a collection of reusable templates.
# Eliminates duplicated generation logic for Risk, Validation and similar
# test case categories.
def generate_from_template(
    analysis,
    template,
    items,
    priority,
    tag,
):

    tests = []

    for item in items:

        if item not in template:
            continue

        tc_type, description, expected = template[item]

        tests.append(
            create_test_case(
                analysis=analysis,
                title=description,
                tc_type=tc_type,
                priority=priority,
                expected_result=expected,
                tags=[tag],
            )
        )

    return tests