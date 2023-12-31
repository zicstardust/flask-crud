from flask import Flask, redirect
from app.database import db
from flask_migrate import Migrate
from app.users import bp_users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fe21e2112ds'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_users, url_prefix='/users')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/index')
def index():
    return redirect ('/users/recovery')
