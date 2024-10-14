from flask import Flask, redirect
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.models import User

# Initialize Flask-Limiter
limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Add CSRF protection
    CSRFProtect(app)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    # Attach the limiter to the app
    limiter.init_app(app)

    # Register routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # In-memory user storage
    app.users = {}

    # Custom error handler for 429 Too Many Requests
    @app.errorhandler(429)
    def ratelimit_handler(e):
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    return app