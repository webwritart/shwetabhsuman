from flask import Blueprint, render_template
from werkzeug.security import check_password_hash, generate_password_hash
import os

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():
    images = []
    path = 'static/images/concept'

    for f in os.listdir(path):
        images.append(path + '/' + f)
    images.sort()
    print(images)

    # for f in os.listdir(path):
    #     im = Image.open(path + '/' + f)

    return render_template('index.html', images=images)
