from models import RequirementCategory

"""
Requirement Detection Rules

Defines the supported requirement categories together with
their detection keywords, risks and validation rules.

The Requirement Analyzer uses this configuration to classify
business requirements without hardcoded conditional logic.
"""

# Central configuration for requirement classification.
# Each entry defines the keywords used for detection together
# with the associated risks and validation rules.
#
# New requirement categories can be introduced by simply adding
# a new configuration block without modifying the analyzer logic.
REQUIREMENT_RULES = {

    RequirementCategory.LOGIN: {

        "keywords": [
            "login",
            "username",
            "password"
        ],

        "risks": [
            "Invalid credentials",
            "Locked account",
            "Empty password"
        ],

        "validations": [
            "Username required",
            "Password required",
            "Username length"
        ]
    },

    RequirementCategory.PASSWORD_RESET: {

        "keywords": [
            "password",
            "reset",
            "email"
        ],

        "risks": [
            "Non-existing email",
            "Expired reset link",
            "Invalid reset token"
        ],

        "validations": [
            "Email required",
            "Valid email format"
        ]
    },

    RequirementCategory.REGISTRATION: {

        "keywords": [
            "register",
            "registration",
            "email",
            "password"
        ],

        "risks": [
            "Duplicate account",
            "Weak password",
            "Invalid email"
        ],

        "validations": [
            "Email required",
            "Password strength",
            "Username required"
        ]
    }

}