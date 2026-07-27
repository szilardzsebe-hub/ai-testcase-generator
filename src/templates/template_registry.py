"""
Template registry

Acts as a central lookup for all reusable 
test case templates.

By separating template seclection from the generator,
the architecture remains modular, maintainable and 
easily extensible for future requirement categories 
and industry-specific templates.

"""

from models import RequirementCategory
from templates.login_preconditions import LOGIN_PRECONDITIONS
from templates.login_test_data import LOGIN_TEST_DATA
from templates.login_steps import LOGIN_STEPS
from templates.login_postconditions import LOGIN_POSTCONDITIONS

PRECONDITIONS_REGISTRY = {
    RequirementCategory.LOGIN: LOGIN_PRECONDITIONS,
}

TESTDATA_REGISTRY = {
    RequirementCategory.LOGIN: LOGIN_TEST_DATA,
}

STEPS_REGISTRY = {
    RequirementCategory.LOGIN: LOGIN_STEPS,
}

POSTCONDITIONS_REGISTRY = {
    RequirementCategory.LOGIN: LOGIN_POSTCONDITIONS,
}

# Represents the supported requirement categories.
# Centralizing categories in an enumeration improves maintainability,
# prevents typographical errors, and simplifies future extensions.


    