from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from app.utils import is_active, is_active_partial
from app.libmain import *
import os

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'img')
    app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024  # 16MB
    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.routes.user import user as user_blueprint
    from app.routes.admin import admin as admin_blueprint

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    @app.errorhandler(400)
    def page_forbidden(e):
        return render_template('400.html'), 400


    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    
    
    app.jinja_env.globals.update(is_active=is_active, is_active_partial=is_active_partial)
    return app
