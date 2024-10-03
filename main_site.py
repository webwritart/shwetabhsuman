import os
# from extensions import db, login_manager
<<<<<<< HEAD
from models.member import Member
=======
# from models.member import Member
>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
from routes.main import main
from routes.gallery import gallery
# from routes.account import account
from routes.manager import manager
from routes.about import about
from flask import Flask
# from dotenv import load_dotenv
# from models.member import Member, Role, member_role

# load_dotenv()

app = Flask(__name__)
app.secret_key = 'erghihogiOEIRTighrGHIER948ERGHr8g(%dgeoi*%J9HL(3grgfgr9KJJK'
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shwetabh.db"


# db.init_app(app)
# login_manager.init_app(app)

# ------------------------------ BLUEPRINTS -------------------------------- #

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(gallery, url_prefix='/gallery')
# app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(manager, url_prefix='/manager')
app.register_blueprint(about, url_prefix='/about')

# with app.app_context():
#     db.create_all()


<<<<<<< HEAD
# @login_manager.user_loader
# def load_user(member_id):
=======
# # @login_manager.user_loader
# # def load_user(member_id):
>>>>>>> fbc20e2b7632053eea779d1148f902826ee6c261
#     return db.get_or_404(Member, member_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
