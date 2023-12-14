from flask import Flask
from database import db
from flask_migrate import Migrate
from users import bp_users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fe21e2112ds'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_users, url_prefix='/users')

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

