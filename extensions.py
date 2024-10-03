from functools import wraps
from flask import abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

# db = SQLAlchemy()
# login_manager = LoginManager()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role.name != 'admin':
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function