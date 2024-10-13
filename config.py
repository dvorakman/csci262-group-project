from os import urandom

class Config:
    SECRET_KEY = 'superduperultrasecretmegabananzatopsecretclearanceonlykey'
    PEPPER = urandom(16)  # Cryptographically secure random pepper value (16 bytes)
