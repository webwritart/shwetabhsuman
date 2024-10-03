# import os
<<<<<<< HEAD
# # from extensions import db
=======
# from extensions import db
>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
# from flask import Blueprint, render_template, request, flash, send_file, redirect, url_for, session
# from werkzeug.security import check_password_hash, generate_password_hash
# from models.member import Member, Role
# from flask_login import current_user, login_required, login_user, logout_user
# from datetime import date
# import random
<<<<<<< HEAD
#
# account = Blueprint('account', __name__, static_folder='static', template_folder='templates/account')
#
# otp = random.randint(1000, 9999)
# today_date = date.today()
#
#
=======

# account = Blueprint('account', __name__, static_folder='static', template_folder='templates/account')

# otp = random.randint(1000, 9999)
# today_date = date.today()


>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
# @account.route('/register', methods=['GET', 'POST'])
# def register():
#     num_list = []
#     result = db.session.query(Member)
<<<<<<< HEAD
#
=======

>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
#     email = request.form.get('username')
#     state = request.form.get('state')
#     result = db.session.execute(db.select(Member).where(Member.email == email))
#     user = result.scalar()
#     if user:
#         flash("You've already signed up with that email, log in instead!", "error")
#         return redirect(url_for('account.login'))
#     hash_and_salted_password = generate_password_hash(
#         request.form.get('password'),
#         method='pbkdf2:sha256',
#         salt_length=8
#     )
<<<<<<< HEAD
#
=======

>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
#     new_user = Member(
#         email=request.form.get('email'),
#         password=hash_and_salted_password,
#         name=request.form.get('name'),
#         phone=request.form.get('phone'),
#         whatsapp=request.form.get('whatsapp'),
#         profession=request.form.get('profession'),
#         sex=request.form.get('sex'),
#         dob=dob,
#         state=state,
#         registration_date=today_date
#     )
#     db.session.add(new_user)
#     db.session.commit()
<<<<<<< HEAD
#
#     login_user(new_user)
#     return redirect(url_for('account.home', name=current_user.name.split()[0]))
#     return render_template("register.html", logged_in=current_user.is_authenticated)
#
#
=======

#     login_user(new_user)
#     return redirect(url_for('account.home', name=current_user.name.split()[0]))
#     return render_template("register.html", logged_in=current_user.is_authenticated)


>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
# @account.route('/login', methods=['GET', 'POST'])
# def login():
#     num_list = []
#     raw_num_list = []
#     result = db.session.query(Member)
#     for user in result:
#         num = user.phone
#         raw_num_list.append(num)
#         if len(num) == 10:
#             user_no = f"91{num}"
#         elif len(num) == 11 and num[0] == '0' or '+':
#             user_no = f'91{num[1:]}'
#         elif len(num) == 12 and num[:2] == '91':
#             user_no = num
#         elif len(num) == 13 and num[:3] == '+91':
#             user_no = num[3:]
#         else:
#             user_no = num
#         num_list.append(user_no)
#     if request.method == 'POST':
#         if request.form.get('password2'):
#             pwd = request.form.get('password2')
#             retype_pwd = request.form.get('retype-password2')
#             if pwd != retype_pwd:
#                 flash("Retyped password did not match! Please try again.", "error")
#                 return render_template('update_account.html')
#             hash_and_salted_password = generate_password_hash(
#                 pwd,
#                 method='pbkdf2:sha256',
#                 salt_length=8
#             )
#             current_user.password = hash_and_salted_password
#             current_user.sex = request.form.get('sex')
#             date_ = request.form.get('date')
#             if len(date_) < 2:
#                 date_ = "0" + date_
#             month = request.form.get('month')
#             if len(month) < 2:
#                 month = "0" + month
#             year = request.form.get('year')
#             current_user.dob = f"{year}-{month}-{date_}"
#             current_user.profession = request.form.get('profession')
#             current_user.state = request.form.get('state')
#             db.session.commit()
#             return redirect(url_for('account.home'))
#         data = request.form.get('email-phone')
#         if '@' in data:
#             email = data
#             result = db.session.execute(db.select(Member).where(Member.email == email))
#             user = result.scalar()
#         else:
#             user_phone = ''
#             ph = data
#             if len(ph) == 10:
#                 phone = f"91{ph}"
#             elif len(ph) == 11 and ph[0] == '0' or '+':
#                 phone = f'91{ph[1:]}'
#             elif len(ph) == 12 and ph[:2] == '91':
#                 phone = ph
#             elif len(ph) == 13 and ph[:3] == '+91':
#                 phone = ph[3:]
#             else:
#                 phone = ph
#             if phone in num_list:
#                 index = num_list.index(phone)
#                 user_phone = raw_num_list[index]
#             result = db.session.execute(db.select(Member).where(Member.phone == user_phone))
#             user = result.scalar()
#         password = request.form.get('password')
<<<<<<< HEAD
#
=======

>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
#         # Email or Phone doesn't exist or password incorrect:
#         if not user:
#             flash("That Email or Phone does not exist, please try again.", category="error")
#         elif not check_password_hash(user.password, password):
#             flash('Password incorrect, please try again.', category='error')
#         else:
#             login_user(user)
#             if 'url' in session:
#                 return redirect(session['url'])
#             if db.session.query(Role).filter(Role.name == 'admin').scalar() in current_user.role:
#                 return redirect(url_for('manager.home'))
#             if not current_user.sex or current_user.sex == '':
#                 return render_template('update_account.html')
#             if request.form.get('prev-page') == 'enroll':
#                 flash("You are successfully logged in. Now proceed to enroll", "success")
#                 return redirect(url_for('payment.home'))
#             return redirect(url_for('account.home', name=current_user.name.split()[0]))
<<<<<<< HEAD
#
#     return render_template("login.html", instruction='login')
#
#
# email_list = []
#
#
=======

#     return render_template("login.html", instruction='login')


# email_list = []


>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
# @account.route('/forgot_password', methods=['GET', 'POST'])
# def forgot_password():
#     if request.method == 'POST':
#         if request.form.get('email'):
#             email = request.form.get('email')
#             email_list.append(email)
#             user_mail_list = []
#             results = db.session.query(Member)
#             for result in results:
#                 user_mail_list.append(result.email)
#             if email in user_mail_list:
#                 send_email_support(subject="Password reset",
#                                    recipients=email_list, body='',
#                                    html=render_template('mails/password_reset_link.html',
#                                                         link=f"http://127.0.0.1:5000/account/set_new_password?otp={otp}"),
#                                    image_dict=image_dict)
#                 return render_template('check_mail_notification.html')
#             else:
#                 flash('No account found with the entered email!', 'error')
<<<<<<< HEAD
#
=======

>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
#         if request.form.get('password'):
#             new_pwd = request.form.get('password')
#             hash_and_salted_password = generate_password_hash(
#                 new_pwd,
#                 method='pbkdf2:sha256',
#                 salt_length=8
#             )
#             result = db.session.execute(db.select(Member).where(Member.email == email_list[0]))
#             user = result.scalar()
#             user.password = hash_and_salted_password
<<<<<<< HEAD
#
=======

>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
#             db.session.commit()
#             login_user(user)
#             flash('New password set successfully!', 'success')
#             mail = render_template('mails/password_reset_notification.html')
#             send_email_support('Password Reset', [current_user.email],
#                                '',
#                                mail, image_dict)
#             return redirect(url_for('account.home'))
<<<<<<< HEAD
#
#     return render_template("forgot_password.html")
#
#
=======

#     return render_template("forgot_password.html")


>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
# @account.route('/set_new_password', methods=['GET', 'POST'])
# def set_new_password():
#     entered_otp = request.args.get('otp')
#     if str(otp) == str(entered_otp):
#         return render_template('set_new_password.html')
#     else:
#         send_email_support('ERROR!!!', ['shwetabh@writart.com'], 'Problem forget password reset', '', '')
#         return redirect(url_for("account.login"))
<<<<<<< HEAD
#
#
=======


>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
# @account.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.home'))
