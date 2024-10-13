from config import Config
from app.utils.security import hash_password, verify_password

def register_user(username: str, password: str) -> bool:
    """Register a new user with the given username and password."""
    try:
        # Check if the username already exists
        with open(Config.USERS_FILE, 'r') as file:
            users = {line.strip().split(":")[0]: line.strip().split(":")[1] for line in file}

        if username in users:
            print(f"{username} already exists.")
            return False

        # Hash the password and get the salt
        result = hash_password(password)

        # Save the username, hashed password, and salt to the file
        with open(Config.USERS_FILE, 'a') as user_file, open(Config.SALTS_FILE, 'a') as salt_file, open(Config.SHADOW_FILE, 'a') as shadow_file:
                user_file.write(f"{username}:{result['hashed_password']}\n")
                salt_file.write(f"{username}:{result['salt']}\n")
                shadow_file.write(f"{username}:{result['hashed_password']}:{result['salt']}\n")

        print(f"{username} registered successfully.")
        return True

    except Exception as e:
        print(f"Error during registration: {e}")
        return False

def authenticate_user(username: str, password: str) -> bool:
    """Authenticate the user by checking the provided username and password."""
    try:
        # Read stored users from the file
        with open(Config.USERS_FILE, 'r') as user_file:
            users = {line.strip().split(":")[0]: (line.strip().split(":")[1], line.strip().split(":")[2]) for line in user_file}

        # Check if the username exists
        if username not in users:
            print(f"{username} does not exist.")
            return False

        # Get the stored hash and salt for the user
        stored_hash, stored_salt = users[username]

        # Check the password
        if verify_password(stored_hash, stored_salt, password):
            print(f"{username} successfully authenticated.")
            return True 
        else:
            print(f"{username} authentication failure.")
            return False

    except Exception as e:
        print(f"Error during authentication: {e}")
        return False