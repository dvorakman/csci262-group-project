from password_validator import PasswordValidator

def password_checker(password: str) -> bool:
    # Create a schema
    schema = PasswordValidator()

    # Add properties to it
    schema.min(8).max(30)       # Minimum and maximum length
    schema.has().uppercase()    # At least one uppercase letter
    schema.has().lowercase()    # At least one lowercase letter
    schema.has().digits()       # At least one digit
    schema.has().no().spaces()  # No spaces allowed
    schema.has().symbols()      # At least on special character

    return schema.validate(password)