from flask import Blueprint, render_template, request, redirect
from app.models import User, db

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

    return redirect('/users/recovery')

@bp_users.route('/recovery')
def recovery():
    users = User.query.all()
    return render_template('users_recovery.html', users=users)

@bp_users.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get(id)
    if request.method == 'GET':
        return render_template('users_update.html', user=user)

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user.name = name
    user.email = email

    if password != '':
        user.password = password
    
    db.session.add(user)
    db.session.commit()

    return redirect('/users/recovery')

@bp_users.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = User.query.get(id)
    if request.method == 'GET':
        return render_template('users_delete.html', user=user)
    
    db.session.delete(user)
    db.session.commit()

    return redirect('/users/recovery')
