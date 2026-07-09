RISK_TEMPLATES = {

    "Invalid credentials": (
        "Negative",
        "Verify login with invalid credentials",
        "Error message displayed"
    ),

    "Locked account": (
        "Negative",
        "Verify login with locked account",
        "Access denied"
    ),

    "Empty password": (
        "Negative",
        "Verify login with empty password",
        "Password is required"
    ),

    "Non-existing email": (
        "Negative",
        "Verify password reset with non-existing email",
        "Error message displayed"
    ),

    "Expired reset link": (
        "Negative",
        "Verify password reset with expired reset link",
        "Reset link expired"
    ),

    "Invalid reset token": (
        "Negative",
        "Verify password reset with invalid reset token",
        "Reset token is invalid"
    ),

    "Duplicate account": (
        "Negative",
        "Verify registration with duplicate account",
        "Registration is rejected"
    ),

    "Weak password": (
        "Negative",
        "Verify registration with weak password",
        "Password does not meet complexity requirements"
    ),

    "Invalid email": (
        "Negative",
        "Verify registration with invalid email",
        "Invalid email format"
    )
}