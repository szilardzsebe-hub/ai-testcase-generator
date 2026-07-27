from models import TestType
VALIDATION_TEMPLATES = {

    "Username required": (
        TestType.VALIDATION,
        "Verify login without username",
        "Username is required"
    ),

    "Password required": (
        TestType.VALIDATION,
        "Verify login without password",
        "Password is required"
    ),

    "Email required": (
        TestType.VALIDATION,
        "Verify password reset without email",
        "Email is required"
    ),

    "Valid email format": (
        TestType.VALIDATION,
        "Verify password reset with invalid email format",
        "Invalid email format"
    )
}