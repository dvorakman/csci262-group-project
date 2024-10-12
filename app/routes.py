from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from app.forms import LoginForm
from app.utils.security import verify_password, hash_password

main_bp = Blueprint('main', __name__)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = current_app.users.get(email)

        if user and verify_password(user['password'], password):
            flash('Login successful, please complete MFA', 'success')
            # Simulating MFA challenge
            return redirect(url_for('main.mfa'))
        
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = hash_password(form.password.data)
        
        # Register the user in the in-memory dictionary
        if email not in current_app.users:
            current_app.users[email] = {'password': password}
            flash('User registered successfully!', 'success')
            return redirect(url_for('main.login'))
        else:
            flash('User already exists!', 'danger')
    
    return render_template('login.html', form=form)

@main_bp.route('/mfa', methods=['GET', 'POST'])
def mfa():
    # Simulate MFA challenge, after login success
    return render_template('dashboard.html')
