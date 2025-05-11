# import os
import os

from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from extensions import db
from flask import Blueprint, render_template, request, flash, send_file, redirect, url_for, session
# from werkzeug.security import check_password_hash, generate_password_hash
from models.member import Member, Role
from operations.miscellaneous import resize_image

# from flask_login import current_user, login_required, login_user, logout_user
# from datetime import date
# import random
#
account = Blueprint('account', __name__, static_folder='static', template_folder='templates/account')


@account.route('/login', methods=['GET', 'POST'])
def login():
    result = db.session.query(Member).all()

    if request.method == 'POST':
        user_emails = []
        data = request.form.get('email')
        password = request.form.get('password')

        for u in result:
            user_emails.append(u.username)

        # Email or Phone doesn't exist or password incorrect:
        if data in user_emails:
            user = db.session.query(Member).filter_by(username=data).scalar()
            if not check_password_hash(user.password, password):
                flash('Password incorrect, please try again.', category='error')
                return redirect(request.url)
            else:
                login_user(user)
                admin = db.session.query(Role).filter_by(name='admin').one()
                if admin in user.role:
                    return redirect(url_for('account.manager', logged_in=current_user.is_authenticated))
        else:
            flash("That Email or Phone does not exist!", category="error")
            return redirect(request.url)

    return render_template("login.html", instruction='login')


@account.route('/manager', methods=['GET', 'POST'])
def manager():
    admin = db.session.query(Role).filter_by(name='admin').one()
    if not current_user.is_authenticated:
        return redirect(url_for('account.login'))
    elif admin in current_user.role:
        return render_template('manager.html', logged_in=current_user.is_authenticated)
    else:
        return redirect(url_for('main.home'))


@account.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@login_required
@account.route('/upload_others', methods=['GET', 'POST'])
def upload_others():
    if request.method == 'POST':
        if request.form.get('submit') == 'upload_other_artworks':
            if 'file' not in request.files:
                flash('No file part', 'error')
                return redirect(request.url)
            files = request.files.getlist('file')

            folder = f"./static/images/others/raw"
            if not os.path.exists(folder):
                os.makedirs(folder)
            for file in files:
                if file.filename == '':
                    flash('No selected file', 'error')
                    return redirect(request.url)
                filename = secure_filename(file.filename)
                file.save(f"{folder}/{filename}")

            output_folder_thumbnail = './static/images/others/thumbnail'
            output_folder_large = './static/images/others/large'

            resize_image(folder, 't', output_folder_thumbnail)
            resize_image(folder, 'f', output_folder_large)
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            flash('Chief! Images uploaded successfully!', 'success')
            return redirect(request.url)
    return redirect(url_for('account.manager', logged_in=current_user.is_authenticated))
