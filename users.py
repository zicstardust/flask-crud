from flask import Blueprint, render_template, request
from models import User
from models import db

bp_users = Blueprint("users", __name__, template_folder="templates")


@bp_users.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'GET':
        return render_template('users_create.html')

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User(name, email, password)
    db.session.add(user)
    db.session.commit()

    return 'create user!'