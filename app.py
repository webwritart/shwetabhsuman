import os
from extensions import db, login_manager
from models.member import Member
from routes.main import main
from routes.gallery import gallery
from routes.account import account
from flask import Flask
from dotenv import load_dotenv
from models.member import Member, Role, member_role

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shwetabh.db"


db.init_app(app)
login_manager.init_app(app)

# ------------------------------ BLUEPRINTS -------------------------------- #

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(gallery, url_prefix='/gallery')
app.register_blueprint(account, url_prefix='/gallery')

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(member_id):
    return db.get_or_404(Member, member_id)


if __name__ == '__main__':
    app.run(debug=True)
