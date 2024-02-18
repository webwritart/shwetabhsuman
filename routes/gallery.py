from flask import Blueprint, render_template


gallery = Blueprint('gallery', __name__, static_folder='static', template_folder='templates/gallery/')


@gallery.route('/')
def home():
    return render_template('gallery.html')


@gallery.route('/character_concept')
def character_concept():
    return render_template('characters.html')


@gallery.route('/environments')
def environments():
    return render_template('environments.html')

