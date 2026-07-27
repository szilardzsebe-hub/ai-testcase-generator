from enum import Enum


class TestType(Enum):
    POSITIVE = "Positive"
    RISK = "Risk"
    BOUNDARY = "Boundary"
    VALIDATION = "Validation"


class Priority(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class AutomationCandidate(Enum):
    YES = "Yes"
    NO = "No"
    PARTIAL = "Partial"

class TestCase:
    def __init__(
        self,
        tc_id,
        title,
        requirement,
        category,
        tc_type,
        priority,
        preconditions,
        test_data,
        steps,
        expected_result,
        postconditions,
        automation_candidate,
        tags,
    ):
        self.tc_id = tc_id
        self.title = title
        self.requirement = requirement
        self.category = category
        self.tc_type = tc_type
        self.priority = priority
        self.preconditions = preconditions
        self.test_data = test_data
        self.steps = steps
        self.expected_result = expected_result
        self.postconditions = postconditions
        self.automation_candidate = automation_candidate
        self.tags = tags

    def to_dict(self):
             return {
                "Test Case ID": self.tc_id,
                "Title": self.title,
                "Requirement": self.requirement,
                "Category": self.category.value,
                "Test Type": self.tc_type.value,
                "Priority": self.priority.value,
                "Preconditions": self.preconditions,
                "Test Data": self.test_data,
                "Steps": self.steps,
                "Expected Result": self.expected_result,
                "Postconditions": self.postconditions,
                "Automation Candidate": self.automation_candidate.value,
                "Tags": self.tags,
            }
# Stores the result of the requirement analysis.
# Besides the detected metadata, the original requirement
# is preserved to maintain full traceability between the
# business requirement and the generated test cases.

class RequirementAnalysis:
    def __init__(self,requirement,category,risks, validations, keywords):
        self.requirement = requirement
        self.category = category
        self.risks = risks
        self.validations = validations
        self.keywords = keywords


# Represents the supported requirement categories.
# Centralizing categories in an enumeration improves maintainability,
# prevents typographical errors, and simplifies future extensions.
class RequirementCategory(Enum):
    LOGIN = "LOGIN"
    REGISTRATION = "REGISTRATION"
    PASSWORD_RESET = "PASSWORD_RESET"
