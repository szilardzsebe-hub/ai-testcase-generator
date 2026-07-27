from templates.template_registry import (
    PRECONDITIONS_REGISTRY,
    TESTDATA_REGISTRY,
    STEPS_REGISTRY,
    POSTCONDITIONS_REGISTRY,
)


def load_templates(category):
    """
    Loads reusable templates for the specified requirement category.

    Returns the predefined preconditions, test data,
    execution steps and postconditions associated
    with the business flow.
    """

    return {
    "preconditions": PRECONDITIONS_REGISTRY.get(category, []),
    "test_data": TESTDATA_REGISTRY.get(category, {}),
    "steps": STEPS_REGISTRY.get(category, []),
    "postconditions": POSTCONDITIONS_REGISTRY.get(category, []),
    }


from models import (
    TestCase,
    AutomationCandidate,
)

def create_test_case(
    analysis,
    title,
    tc_type,
    priority,
    expected_result,
    tags,
):

    templates = load_templates(analysis.category)

    return TestCase(
        tc_id=None,
        title=title,
        requirement=analysis.requirement,
        category=analysis.category,
        tc_type=tc_type,
        priority=priority,
        preconditions=templates["preconditions"],
        test_data=templates["test_data"],
        steps=templates["steps"],
        expected_result=expected_result,
        postconditions=templates["postconditions"],
        automation_candidate=AutomationCandidate.YES,
        tags=tags,
    )
# Represents the supported requirement categories.
# Centralizing categories in an enumeration improves maintainability,
# prevents typographical errors, and simplifies future extensions.