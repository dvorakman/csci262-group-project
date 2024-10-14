from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import LoginForm, RegisterForm, MFAForm
from app.utils.security import verify_password, generate_unique_user_id, hash_password, password_checker
from app.utils.register_users import register_user
from app.models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return redirect(url_for('main.mfa'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_data = current_app.users.get(username)
    
        if user_data and verify_password(user_data['password']['hashed_password'], user_data['password']['salt'], password):
            user = User(user_data['id'], username, user_data['password'])
            login_user(user)
            flash('Login successful, please complete MFA', 'success')
            return redirect(url_for('main.mfa'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if password_checker(password):
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            hashed_password = hash_password(password)
            
            if username not in current_app.users:
                user_id = generate_unique_user_id()
                current_app.users[username] = {
                    'id': user_id,
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': hashed_password
                }
                flash('Registration successful, please log in', 'success')
                return redirect(url_for('main.login'))
            else:
                flash('Username already exists', 'danger')
        else:
            flash('Password does not meet security requirements', 'danger')
    return render_template('register.html', form=form)

@main_bp.route('/mfa', methods=['GET', 'POST'])
@login_required
def mfa():
    form = MFAForm()
    if form.validate_on_submit():
        flash('MFA completed successfully!', 'success')
        return render_template('dashboard.html')
    return render_template('mfa.html', form=form)

@main_bp.route('/list_users', methods=['GET'])
@login_required
def list_users():
    return render_template('list_users.html', users=current_app.users)

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.login'))