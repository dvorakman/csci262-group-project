from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def mfa_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.mfa_completed:
            flash('Please complete MFA setup.', 'warning')
            return redirect(url_for('main.mfa'))
        return f(*args, **kwargs)
    return decorated_function