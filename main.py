from wtforms.validators import Length, Regexp

def password_checker() -> bool:
    # Define the validators
    length_validator = Length(min=8, max=30, message="Password must be between 8 and 30 characters long.")
    
    uppercase_validator = Regexp(r'[A-Z]', message="Password must contain at least one uppercase letter.")
    lowercase_validator = Regexp(r'[a-z]', message="Password must contain at least one lowercase letter.")
    digit_validator = Regexp(r'\d', message="Password must contain at least one digit.")
    no_space_validator = Regexp(r'^\S*$', message="Password must not contain any spaces.")

    special_char_validator = Regexp(r'[!@#$%^&*(),.?":{}|<>]', message="Password must contain at least one special character.")

    # Combine the validators
    validator_list = [
        length_validator,
        uppercase_validator,
        lowercase_validator,
        digit_validator,
        no_space_validator,
        special_char_validator
    ]

    return validator_list