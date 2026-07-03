from models import TestCase
from requirement_analyzer import analyze_requirement



def generate_test_cases(requirement):

    analysis = analyze_requirement(requirement)
    

    if analysis.category == "PASSWORD_RESET":
        return [
            TestCase(None, "Positive", "Verify password reset with valid email", "Password reset email is sent"),
            TestCase(None, "Negative", "Verify password reset with non-existing email", "Error message displayed"),
            TestCase(None, "Boundary", "Verify password reset with maximum email length", "Request handled correctly")
        ]

    elif analysis.category == "LOGIN":
        return [
            TestCase(None, "Positive", "Verify login with valid email", "User is logged in successfully"),
            TestCase(None, "Negative", "Verify login with invalid email", "Error message displayed"),
            TestCase(None, "Boundary", "Verify login with maximum email length", "Request handled correctly")
        ]

    elif analysis.category == "REGISTRATION":
        return [
            TestCase(None, "Positive", "Verify registration with valid email", "User is registered successfully"),
            TestCase(None, "Negative", "Verify registration with invalid email", "Error message displayed"),
            TestCase(None, "Boundary", "Verify registration with maximum email length", "Request handled correctly")
        ]

    else:
        return [
            TestCase(None, "Positive", f"Verify successful flow for: {requirement}", "System behaves as expected")
        ]
