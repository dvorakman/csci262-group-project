from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, session
from app.forms import LoginForm, RegisterForm
from app.utils.security import verify_password, hash_password
import uuid

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' in session:
        return redirect(url_for('main.mfa'))
    else:
        return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userid = form.userid.data
        password = form.password.data
        user = current_app.users.get(userid)

        if user and verify_password(user['password'], password):
            session['user_id'] = user['id']
            flash('Login successful, please complete MFA', 'success')
            return redirect(url_for('main.mfa'))
        
        flash('Invalid userid or password', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        userid = form.userid.data
        password = hash_password(form.password.data)
        
        # Register the user in the in-memory dictionary
        if userid not in current_app.users:
            user_id = generate_unique_user_id()  # Function to generate a unique user ID
            current_app.users[userid] = {'id': user_id, 'password': password}
            flash('User registered successfully!', 'success')
            return redirect(url_for('main.login'))
        else:
            flash('User already exists!', 'danger')
    return render_template('register.html', form=form)

@main_bp.route('/mfa', methods=['GET', 'POST'])
def mfa():
    # Simulate MFA challenge, after login success
    return render_template('dashboard.html')

def generate_unique_user_id():
    # Implement a function to generate a unique user ID
    return str(uuid.uuid4())