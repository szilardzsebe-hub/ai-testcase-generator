from models import TestType
POSITIVE_TEMPLATES = {

    "LOGIN": (
        TestType.POSITIVE,
        "Verify successful login with valid credentials",
        "User is logged in successfully"
    ),

    "PASSWORD_RESET": (
        TestType.POSITIVE,
        "Verify password reset with valid email",
        "Password reset email is sent"
    ),

    "REGISTRATION": (
        TestType.POSITIVE,
        "Verify registration with valid email",
        "User is registered successfully"
    )
}