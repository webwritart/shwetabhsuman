from flask import Blueprint, render_template, url_for

about = Blueprint('about', __name__, static_folder='static', template_folder='templates/about')


@about.route('/about', methods=['GET', 'POST'])
def home():

    return render_template('about.html')