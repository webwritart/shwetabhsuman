import pprint
import random
# from extensions import db
# from models.member import Member, Role
from flask import Blueprint, render_template, request, flash, redirect
from werkzeug.security import check_password_hash, generate_password_hash
import os
from datetime import datetime
from operations.messenger import send_email

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():
    # print(images)

    # for f in os.listdir(path):
    #     im = Image.open(path + '/' + f)
    current_year = datetime.now().year
    return render_template('index.html', current_year=current_year)


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
    return render_template('other_works.html', bottom_menu=top_bottom_menu, page=page, dict=artist_dict_shuffled)


@main.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')


@main.route('/3d')
def three_d():
    return render_template('3d.html')


@main.route('/composition')
def composition():
    col = ['#d9d9d9', '#d9d9d9', '#d9d9d9', 'white']
    top_bottom_menu = 'y'
    return render_template('composition.html', col=col, bottom_menu=top_bottom_menu)


@main.route('/illustrations')
def illustrations():
    page = 'other_works'
    top_bottom_menu = 'y'
    return render_template('illustrations.html', page=page, bottom_menu=top_bottom_menu)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        email2 = request.form.get('email2')
        msg = request.form.get('message')
        message = f'{msg}\n\n\nSENDER DETAILS:\nName: {name}\nEmail: {email}\n'

        success_msg = (f'Dear {name},\n\nThanks for sending me a message.\nI will get back to you as soon as possible. '
                       f':)\n\n\nShwetabh Suman\nConcept Artist & Illustrator\nNew Delhi, India')

        spam_test_1 = 'http://'
        spam_test_2 = 'https://'
        if spam_test_1 or spam_test_2 not in name:
            if email == email2:
                send_email('IMPORTANT!! - Main Portfolio', ['shwetabhartist@gmail.com'], email, message, '', '')
                send_email('MESSAGE SENT - Shwetabh Suman', [email], 'shwetabhartist@gmail.com', success_msg, '', '')
                flash('Message sent successfully!', 'success')
            else:
                flash("The email doesn't match!", "error")
                return redirect(request.url)
    return render_template('contact.html')
