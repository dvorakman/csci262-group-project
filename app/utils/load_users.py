from app.utils.security import hash_password, generate_unique_user_id

def load_user_database():
    default_users = [
        {
            'first_name': 'Admin',
            'last_name': 'User',
            'email': 'admin@admin.com',
            'username': 'admin',
            'password': 'admin'
        },
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'username': 'johndoe',
            'password': 'Password123!'
        },
        {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'username': 'janesmith',
            'password': 'SecurePass456@'
        },
        {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'email': 'alice.johnson@example.com',
            'username': 'alicejohnson',
            'password': 'Alice789#'
        }
    ]

    store = {}

    for user in default_users:
        # Hash the password
        hashed_password = hash_password(user['password'])
        
        # Generate a unique user ID
        user_id = generate_unique_user_id()
        
        # Add user to the in-memory database
        store[user['username']] = {
            'id': user_id,
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'password': hashed_password
        }

    return store