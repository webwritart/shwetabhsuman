import pprint
import random

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


@main.route('/other_works')
def other_works():
    page = 'other_works'
    top_bottom_menu = 'y'
    artist_dict = {}
    artist_dict_shuffled = {}
    artworks_thumbnail_dir = f'static/images/others/thumbnail/'
    artworks_large_dir = f'static/images/others/large/'
    index = 1
    for entry in os.scandir(artworks_thumbnail_dir):
        if entry.is_file():
            root, ext = os.path.splitext(entry.name)
            base_name = root[:-1]
            f_size_file_name = base_name + 'f' + ext
            thumbnail_path = f'/{artworks_thumbnail_dir}{entry.name}'
            large_path = f'/{artworks_large_dir}{f_size_file_name}'
            title = os.path.splitext(os.path.basename(entry.name))[0][:-2]
            img = {
                'title': title,
                'thumbnail': thumbnail_path,
                'large': large_path
            }
            artist_dict[index] = img
            index += 1
    keys = list(artist_dict.keys())
    random.shuffle(keys)
    for key in keys:
        item = artist_dict[key]
        artist_dict_shuffled[key] = item
    print(artist_dict_shuffled)
    return render_template('other_works.html', bottom_menu=top_bottom_menu, page=page, dict=artist_dict_shuffled)


@main.route('/composition')
def composition():
    col = ['#d9d9d9', '#d9d9d9', '#d9d9d9', 'white']
    top_bottom_menu = 'y'
    return render_template('composition.html', col=col, bottom_menu=top_bottom_menu)
