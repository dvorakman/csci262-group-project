import uuid
import hashlib
from os import urandom
import base64
from config import Config
from password_validator import PasswordValidator

def hash_password(password: str):
    """Hash the given password with a random salt and a pepper."""
    # Convert the password to bytes and generate a random 16-byte salt
    password_bytes = password.encode()
    salt = urandom(16)

    # Combine password, salt and pepper, then hash using SHA-256
    password_with_salt_and_pepper = password_bytes + salt + Config.PEPPER
    hashed_password = hashlib.sha256(password_with_salt_and_pepper).digest()

    return {
        'salt': base64.b64encode(salt).decode('utf-8'),
        'hashed_password': base64.b64encode(hashed_password).decode('utf-8')
    }


def verify_password(stored_hash: base64, stored_salt: base64 = "", password: str=""):
    """Verify the given password against the stored hash and salt."""
    # Convert the password to bytes and decode the stored salt and hash
    password_bytes = password.encode('utf-8')
    salt = base64.b64decode(stored_salt)
    stored_hash_bytes = base64.b64decode(stored_hash)

    # Hash the password with the stored salt and pepper
    password_with_salt_and_pepper = password_bytes + salt + Config.PEPPER
    hashed_password = hashlib.sha256(password_with_salt_and_pepper).digest()

    return hashed_password == stored_hash_bytes


def generate_unique_user_id():
    # Implement a function to generate a unique user ID
    return str(uuid.uuid4())

def password_checker(password: str) -> bool:
    # Create a schema
    schema = PasswordValidator()

    # Add properties to the schema
    schema.has().uppercase()    # At least one uppercase letter
    schema.has().lowercase()    # At least one lowercase letter
    schema.has().digits()       # At least one digit
    schema.has().no().spaces()  # No spaces allowed
    schema.has().symbols()      # At least one special character

    # Validate the password based on the schema
    return schema.validate(password)