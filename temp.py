import os

from werkzeug.security import generate_password_hash
from PIL import Image
from main_site import app
from operations.miscellaneous import resize_image

# DIR = 'static/images/others/'
# output_folder = 'static/images/others/thumbnail'
#
# resize_image(DIR, 't')
# pwd = '@x010319944551S'
# hash_and_salted_password = generate_password_hash(
#     pwd,
#     method='pbkdf2:sha256',
#     salt_length=8
# )
# print(hash_and_salted_password)
# with app.app_context():
#     user = db.session.query(Member).filter_by(name='Shwetabh Suman').scalar()
#     admin = db.session.query(Role).filter_by(name='admin').scalar()
#     if admin in user.role:
#         print('yes')

