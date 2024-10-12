from werkzeug.security import generate_password_hash, check_password_hash
import uuid

def hash_password(password):
    return generate_password_hash(password)

def verify_password(stored_hash, password):
    return check_password_hash(stored_hash, password)

def generate_unique_user_id():
    # Implement a function to generate a unique user ID
    return str(uuid.uuid4())