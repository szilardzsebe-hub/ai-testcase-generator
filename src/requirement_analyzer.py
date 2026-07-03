from models import RequirementAnalysis


def analyze_requirement(requirement):
    req = requirement.lower()

    if "login" in req:
        return RequirementAnalysis(
            category="LOGIN",
            keywords=["login", "username", "password"],
            risks=[
                "Invalid credentials",
                "Locked account",
                "Empty password"
            ],
            validations=[
                "Username required",
                "Password required",
                "Username length"
            ]
        )

    elif "password" in req:
        return RequirementAnalysis(
            category="PASSWORD_RESET",
            keywords=["password", "email", "reset"],
            risks=[
                "Invalid email",
                "Expired reset link",
                "Empty email"
            ],
            validations=[
                "Email required",
                "Email format",
                "Maximum email length"
            ]
        )

    elif "register" in req or "registration" in req:
        return RequirementAnalysis(
            category="REGISTRATION",
            keywords=["register", "email", "password"],
            risks=[
                "Duplicate account",
                "Weak password",
                "Invalid email"
            ],
            validations=[
                "Email required",
                "Password strength",
                "Email format"
            ]
        )

    return RequirementAnalysis(
        category="GENERIC",
        keywords=[],
        risks=[],
        validations=[]
    )