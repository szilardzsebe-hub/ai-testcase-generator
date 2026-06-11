from models import TestCase


def generate_test_cases(requirement):
    
    req = requirement.lower()

    print(f"Input: {req}")

    if "password" in req:
        return [
            TestCase(
                "TC-001",
                "Positive",
                "Verify password reset with valid email",
                "Password reset email is sent"
            ),
            TestCase(
                "TC-002",
                "Negative",
                "Verify password reset with non-existing email",
                "Error message displayed"
            ),
            TestCase(
                "TC-003",
                "Boundary",
                "Verify password reset with maximum email length",
                "Request handled correctly"
            )
        ]


    elif "login" in req:
        return [
            TestCase(
                "TC-001",
                "Positive",
                "Verify login  with valid email",
                "User is logged in successfully"
            ),
            TestCase(
                "TC-002",
                "Negative",
                "Verify login with invalid email",
                "Error message displayed"
            ),
            TestCase(
                "TC-003",
                "Boundary",
                "Verify login with maximum email length",
                "Request handled correctly"
            )
        ]

    elif "register" in req or "registration" in req:
        return [
            TestCase(
                "TC-001",
                "Positive",
                "Verify registration with valid email",
                "User is registered successfully"
            ),
            TestCase(
                "TC-002",
                "Negative",
                "Verify registration with invalid email",
                "Error message displayed"
            ),
            TestCase(
                "TC-003",
                "Boundary",
                "Verify registration with maximum email length",
                "Request handled correctly"
            )
        ]
    else:
     return [
        TestCase(
            "TC-001",
            "Positive",
            f"Verify successful flow for: {requirement}",
            "System behaves as expected"
        )
    ]