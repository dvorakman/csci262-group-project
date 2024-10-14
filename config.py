from os import urandom

class Config:
    SECRET_KEY = 'superduperultrasecretmegabananzatopsecretclearanceonlykey'
    PEPPER = urandom(16)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'Lax'