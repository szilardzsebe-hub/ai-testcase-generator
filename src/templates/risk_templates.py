from models import TestType

RISK_TEMPLATES ={  
    

    "Invalid credentials": (
        TestType.RISK,
        "Verify login with invalid credentials",
        "Error message displayed"
    ),

    "Locked account": (
        TestType.RISK,
        "Verify login with locked account",
        "Access denied"
    ),

    "Empty password": (
        TestType.RISK,
        "Verify login with empty password",
        "Password is required"
    ),

    "Non-existing email": (
        TestType.RISK,
        "Verify password reset with non-existing email",
        "Error message displayed"
    ),

    "Expired reset link": (
        TestType.RISK,
        "Verify password reset with expired reset link",
        "Reset link expired"
    ),

    "Invalid reset token": (
        TestType.RISK,
        "Verify password reset with invalid reset token",
        "Reset token is invalid"
    ),

    "Duplicate account": (
        TestType.RISK,
        "Verify registration with duplicate account",
        "Registration is rejected"
    ),

    "Weak password": (
        TestType.RISK,
        "Verify registration with weak password",
        "Password does not meet complexity requirements"
    ),

    "Invalid email": (
        TestType.RISK,
        "Verify registration with invalid email",
        "Invalid email format"
    )
}
