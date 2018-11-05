import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from base import db
from base import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.session.query(User.query.filter(User.username == username).exists()).scalar():
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.session.add(User(username=username, password=password))
            db.session.commit()
            return redirect(url_for('auth.register_succesful'))

        flash(error)

    return render_template('register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        if not db.session.query(User.query.filter(User.username == username).exists()).scalar():
            error = 'User or password is not valid.'
        else:
            user = db.session.query(User).filter(User.username == username).one()
            if user.password != request.form['password']:
                error = 'User or password is not valid.'

        if error is None:
            return redirect(url_for('auth.register_succesful'))

        flash(error)

    return render_template('login.html')


@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        username = request.form['username']
        newpw = request.form['newpassword']
        newpw2 = request.form['newpassword2']
        error = None

        if not username:
            error = 'Username is required.'

        if not username:
            error = 'New password is required.'

        if not newpw == newpw2:
            error = 'Password not match'

        elif not db.session.query(User.query.filter(User.username == username).exists()).scalar():
            error = 'User {} is not registered.'.format(username)

        if error is None:
            User.query.filter_by (username=username).update (dict (password=newpw))
            db.session.commit ()

            return redirect(url_for('auth.register_succesful'))

        flash(error)

    return render_template('edit.html')

@bp.route('/register_succesful')
def register_succesful():
    return render_template('register_success.html')
