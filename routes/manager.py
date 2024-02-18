from flask import Blueprint,render_template


manager = Blueprint('manager', __name__, static_folder='static', template_folder='templates/manager')


@manager.route('/')
def home():
    return render_template('manager.html')

