from models import RequirementAnalysis, RequirementCategory
from requirement_rules import REQUIREMENT_RULES


def analyze_requirement(requirement):

    req = requirement.lower()

    for category, rule in REQUIREMENT_RULES.items():

        if any(keyword in req for keyword in rule["keywords"]):

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