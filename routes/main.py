from flask import Blueprint, render_template
from werkzeug.security import check_password_hash, generate_password_hash
import os
from datetime import datetime

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():

    # print(images)

    # for f in os.listdir(path):
    #     im = Image.open(path + '/' + f)
    current_year = datetime.now().year
    return render_template('index.html',current_year=current_year)


@main.route('/game_world_plan')
def game_world_plan():
    page = 'world'
    top_bottom_menu = 'y'
    return render_template('game_world_plan.html',bottom_menu=top_bottom_menu, page=page)


@main.route('/character_concept')
def character_concept():
    page = 'characters'
    top_bottom_menu = 'y'
    return render_template('character_concept.html', bottom_menu=top_bottom_menu, page=page)


@main.route('/environment_concept')
def environment_concept():
    page = 'environment'
    top_bottom_menu = 'y'
    return render_template('environment_concept.html', bottom_menu=top_bottom_menu, page=page)


@main.route('/composition')
def composition():
    col = ['#d9d9d9', '#d9d9d9', '#d9d9d9', 'white']
    top_bottom_menu = 'y'
    return render_template('composition.html', col=col, bottom_menu=top_bottom_menu)
