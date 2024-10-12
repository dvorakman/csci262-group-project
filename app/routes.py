from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, session
from app.forms import LoginForm, RegisterForm, MFAForm
from app.utils.security import verify_password, generate_unique_user_id
from utils.register_users import register_user
from utils.security import hash_password
from base64 import b64encode

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    user_id = session.get('user_id')
    if user_id and any(user['id'] == user_id for user in current_app.users.values()):
        return redirect(url_for('main.mfa'))
    else:
        session.clear()  # Clear the session if the user ID is not valid
        return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = current_app.users.get(username)

        if user and verify_password(user['password'], password):
            session['user_id'] = user['id']
            session['logged_in'] = True  # Set session token
            flash('Login successful, please complete MFA', 'success')
            return redirect(url_for('main.mfa'))
        
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            username = form.username.data
            password = hash_password(form.password.data)
            
            # Register the user in the in-memory dictionary
            if username not in current_app.users:
                user_id = generate_unique_user_id()  # Function to generate a unique user ID
                current_app.users[username] = {
                    'id': user_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': password
                }

            if register_user(username, password):
                 flash('User registered successfully!', 'success')
            else:
                flash('User already exists!', 'danger')
        
            
            return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main_bp.route('/mfa', methods=['GET', 'POST'])
def mfa():
    if not session.get('logged_in'):
        flash('You must log in first.', 'danger')
        return redirect(url_for('main.login'))
    
    form = MFAForm()
    if form.validate_on_submit():
        # Assume MFA is completed successfully
        session.pop('logged_in', None)  # Clear session token
        flash('MFA completed successfully!', 'success')
        return render_template('dashboard.html')
    
    return render_template('mfa.html', form=form)

@main_bp.route('/list_users', methods=['GET'])
def list_users():
    return render_template('list_users.html', users=current_app.users)