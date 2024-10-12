from password_validator import PasswordValidator

def password_checker(password: str) -> bool:
    # Create a schema
    schema = PasswordValidator()

    # Add properties to it
    schema.min(8)
    schema.max(30)
    schema.has().uppercase()
    schema.has().lowercase()
    schema.has().digits()
    schema.has().no().spaces()
    return schema.validate(password)