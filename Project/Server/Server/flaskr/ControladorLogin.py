from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.base import *
urlLogin = Blueprint('ControladorLogin', __name__, url_prefix='/ControladorLogin')
#
@urlLogin.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        if not db.session.query(Usuario.query.filter(Usuario.username == username).exists()).scalar():
            error = 'User or password is not valid.'
        else:
            user = db.session.query(Usuario).filter(Usuario.username == username).one()
            if user.password != request.form['password']:
                error = 'User or password is not valid.'
        if error is None:
            session.clear()
            session["user"] = username
            session["auth"] = 1
            return redirect(url_for('auth.login_succesful'))
        flash(error)
    return render_template('login.html')