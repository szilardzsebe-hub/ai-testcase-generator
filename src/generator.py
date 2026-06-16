from models import TestCase
from tc_id_service import next_tc_id
from tc_id_service import init_db




from models import TestCase

def generate_test_cases(requirement):
    req = requirement.lower()

    if "reset password" in req:
        return [
            TestCase(None, "Positive", "Verify password reset with valid email", "Password reset email is sent"),
            TestCase(None, "Negative", "Verify password reset with non-existing email", "Error message displayed"),
            TestCase(None, "Boundary", "Verify password reset with maximum email length", "Request handled correctly")
        ]

    elif "login" in req:
        return [
            TestCase(None, "Positive", "Verify login with valid email", "User is logged in successfully"),
            TestCase(None, "Negative", "Verify login with invalid email", "Error message displayed"),
            TestCase(None, "Boundary", "Verify login with maximum email length", "Request handled correctly")
        ]

    elif "register" in req or "registration" in req:
        return [
            TestCase(None, "Positive", "Verify registration with valid email", "User is registered successfully"),
            TestCase(None, "Negative", "Verify registration with invalid email", "Error message displayed"),
            TestCase(None, "Boundary", "Verify registration with maximum email length", "Request handled correctly")
        ]

    else:
        return [
            TestCase(None, "Positive", f"Verify successful flow for: {requirement}", "System behaves as expected")
        ]