from os import urandom

class Config:
    SECRET_KEY = 'superduperultrasecretmegabananzatopsecretclearanceonlykey'
    PEPPER = urandom(16)  # Cryptographically secure random pepper value (16 bytes)
    USERS_FILE = 'users.txt'  # File to store usernames and hashed passwords
    SALTS_FILE = 'salts.txt'
    SHADOW_FILE = 'shadow.txt'
