from src.models import TestType


BOUNDARY_TEMPLATES = {

    "LOGIN": (
        TestType.BOUNDARY,
        "Verify login with maximum username length",
        "Request handled correctly"
    ),

    "PASSWORD_RESET": (
        TestType.BOUNDARY,
        "Verify password reset with maximum email length",
        "Request handled correctly"
    ),

    "REGISTRATION": (
        TestType.BOUNDARY,
        "Verify registration with maximum username length",
        "Request handled correctly"
    ),
}