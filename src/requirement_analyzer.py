from src.models import RequirementAnalysis, RequirementCategory
from src.requirement_rules import REQUIREMENT_RULES


def analyze_requirement(requirement):

    """
    Analyzes a business requirement and classifies it into a supported
    requirement category.

    Returns a RequirementAnalysis object containing detected
    risks, validations and keywords.
    """
    normalized_requirement = requirement.lower()

    for category, rule in REQUIREMENT_RULES.items():

        if any(keyword in normalized_requirement for keyword in rule["keywords"]):

            return RequirementAnalysis(
                requirement=requirement,
                category=category,
                risks=rule["risks"],
                validations=rule["validations"],
                keywords=rule["keywords"]
            )

    return RequirementAnalysis(
        requirement=requirement,
        category=RequirementCategory.GENERIC,
        risks=[],
        validations=[],
        keywords=[]
    )