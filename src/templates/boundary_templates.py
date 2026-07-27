from models import TestType


BOUNDARY_TEMPLATES = {

    "LOGIN": (
        TestType.RISK,
        "Verify login with maximum username length",
        "Request handled correctly"
    ),

    "PASSWORD_RESET": (
        TestType.RISK,
        "Verify password reset with maximum email length",
        "Request handled correctly"
    ),

    "REGISTRATION": (
        TestType.RISK,
        "Verify registration with maximum username length",
        "Request handled correctly"
    ),
}