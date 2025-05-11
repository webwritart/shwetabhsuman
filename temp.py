import os

from werkzeug.security import generate_password_hash
from PIL import Image
from main_site import app
from models.member import Role, Member
from operations.miscellaneous import resize_image
from extensions import db

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
# with app.app_context():
#     user = db.session.query(Member).filter_by(name='Shwetabh Suman').scalar()
#     role = db.session.query(Role).filter_by(name='admin').scalar()
#     user.role.append(role)
#
#     db.session.commit()

