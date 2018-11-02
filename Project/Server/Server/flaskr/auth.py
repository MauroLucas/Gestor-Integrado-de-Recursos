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
            db.session.add(User(username='gian_nativo', password='123456'))
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('register.html')
