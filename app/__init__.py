from flask import Flask
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from app.models import User

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

    # Register routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # In-memory user storage
    app.users = {}
    
    return app