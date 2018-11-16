from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
#
urlRegistrarUsuario = Blueprint('ControladorRegistrarUsuario', __name__, url_prefix='/ControladorRegistrarUsuario')


@urlRegistrarUsuario.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        mail = request.form['mail']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.session.query(Usuario.query.filter(Usuario.username == username).exists()).scalar():
            error = 'User {} is already registered.'.format(username)
        if error is None:
            db.session.add(Usuario( username=username, password=password,nombre=nombre,apellido=apellido,mail=mail))
            db.session.commit()
            return redirect(url_for('auth.register_succesful'))
        flash(error)
    return render_template('register.html')