from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from base import db
from base import Usuario
from base import DatosUsuario
from base import Contacto
from flask import session
from base import *

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
        elif db.session.query(Usuario.query.filter(Usuario.username == username).exists()).scalar():
            error = 'User {} is already registered.'.format(username)

        if error is None:

            db.session.add(Usuario(id_datosUsuario=1, username=username, password=password))
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
        if not db.session.query(Usuario.query.filter(Usuario.username == username).exists()).scalar():
            error = 'User or password is not valid.'
        else:
            user = db.session.query(Usuario).filter(Usuario.username == username).one()
            if user.password != request.form['password']:
                error = 'User or password is not valid.'

        if error is None:
            session['username']=username
            session['password']=password
            return redirect(url_for('auth.login_succesful'))

        flash(error)

    return render_template('login.html')


@bp.route('/register_succesful')
def register_succesful():
    return render_template('register_success.html')

@bp.route('/login_succesful')
def login_succesful():
    return render_template('login_success.html')

@bp.route('/enter_resource', methods=('GET', 'POST'))
def enter_resource():
    if request.method == 'POST':
        resource = request.form['resource']
        description = request.form['description']
        error = None

        if not resource:
            error = 'Resource is required.'

        if error is None:
            db.session.add(Recurso(recurso=resource, descripcion=description))
            db.session.commit()
            return redirect(url_for('auth.login_succesful'))
        flash(error)


    return render_template('enter_resource.html')

@bp.route('/create_group', methods=('GET', 'POST'))
def create_group():

    if request.method == 'POST':
        group_name=request.form['group_name']
        error = None

        if not group_name:
            error = 'Group_name is required.'

        if error is None:

            #user =session.query(Usuario).filter_by(name=session['username']).first()
            db.session.add(Grupo(nombre=group_name , id_admin=6))
            db.session.commit()
    return render_template('create_group.html')
