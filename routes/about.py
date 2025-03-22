from flask import Blueprint, render_template, url_for, request

about = Blueprint('about', __name__, static_folder='static', template_folder='templates/about')


@about.route('/about', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        subject = request.form.get('subject')
        email = request.form.get('mail')
        # file = request.files
    return render_template('about.html')


@about.route('/illustrations', methods=['GET', 'POST'])
def illustrations():
    return render_template('illustrations.html')
