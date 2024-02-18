from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


account = Blueprint('account', __name__, static_folder='static', template_folder='templates/account')


@account.route('/login')
def login():
    return render_template('login.html')


@account.route('/register')
def register():
    return render_template('register.html')


@login_required
@account.route('/logout')
def logout():
    return redirect(url_for('main.home'))
