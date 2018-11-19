from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *

urlEditUsuario = Blueprint('ControladorEditUsuario', __name__, url_prefix='/ControladorEditUsuario')

@urlEditUsuario.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        username = session["user"]
        newpw = request.form['newpassword']
        newpw2 = request.form['newpassword2']
        error = None
        if not newpw:
            error = 'New password is required.'
        if not newpw == newpw2:
            error = 'Password not match'
        elif not db.session.query(Usuario.query.filter(Usuario.username == username).exists()).scalar():
            error = 'User {} is not registered.'.format(username)
        if error is None:
            Usuario.query.filter_by(username=username).update(dict(password=newpw))
            db.session.commit()
            return redirect(url_for('auth.register_succesful'))
        flash(error)
    return render_template('edit.html')