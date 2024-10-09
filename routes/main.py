from flask import Blueprint, render_template
from werkzeug.security import check_password_hash, generate_password_hash
import os

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():

    # print(images)

    # for f in os.listdir(path):
    #     im = Image.open(path + '/' + f)
    col = ['#d9d9d9', '#d9d9d9', '#d9d9d9', '#d9d9d9']

    return render_template('index.html', col=col)


@main.route('/game_world_plan')
def game_world_plan():
    col = ['white', '#d9d9d9', '#d9d9d9', '#d9d9d9']
    bottom_menu = 'y'
    return render_template('game_world_plan.html', col=col, bottom_menu=bottom_menu)


@main.route('/character_concept')
def character_concept():
    col = ['#d9d9d9', 'white', '#d9d9d9', '#d9d9d9']
    bottom_menu = 'y'
    return render_template('character_concept.html', col=col, bottom_menu=bottom_menu)


@main.route('/environment_concept')
def environment_concept():
    col = ['#d9d9d9', '#d9d9d9', 'white', '#d9d9d9']
    bottom_menu = 'y'
    return render_template('environment_concept.html', col=col, bottom_menu=bottom_menu)


@main.route('/composition')
def composition():
    col = ['#d9d9d9', '#d9d9d9', '#d9d9d9', 'white']
    bottom_menu = 'y'
    return render_template('composition.html', col=col, bottom_menu=bottom_menu)
