from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, json, jsonify)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
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
            contacto = Contacto()
            db.session.add(contacto)
            db.session.flush()
            datos_usuario = DatosUsuario(id_contacto=contacto.id_contacto)
            db.session.add(datos_usuario)
            db.session.flush()
            db.session.add(Usuario(id_datosUsuario=datos_usuario.id_datosUsuario, username=username, password=password))
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
            session.clear()
            session["user"] = username
            return redirect(url_for('auth.login_succesful'))
        flash(error)
    return render_template('login.html')


@bp.route('/edit', methods=('GET', 'POST'))
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
            return redirect(url_for('auth.login_succesful'))
        flash(error)
    return render_template('edit.html')


@bp.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    session.pop('user', None)
    return redirect(url_for('main.home'))


@bp.route('/login_succesful')
def login_succesful():
    user = db.session.query(Usuario).filter(Usuario.username == session['user']).one()
    return render_template('user_page.html', categorias=get_user_categories(user))


@bp.route('/create_group', methods=('GET', 'POST'))
def create_group():
    if request.method == 'POST':
        group_name = request.form['group_name']
        error = None
        if not group_name:
            error = 'Group_name is required.'
        if error is None:
            # user = session.query(Usuario).filter_by(name=session['username']).first()
            db.session.add(Grupo(nombre=group_name, id_admin=6))
            db.session.commit()
    return render_template('create_group.html')


@bp.route('/get_group_data', methods=('GET', 'POST'))
def get_group_data():
    content = json.loads(request.data)
    grupo = db.session.query(Grupo).filter(Grupo.id_grupo == int(content['data'])).one()
    usuarios = grupo.usuarios
    #comentarios = db.session.query(Comentario).filter(Comentario.id_grupo == grupo.id_grupo)
    comments = []
    participantes = []
    for usuario in usuarios:
        participantes.append(usuario.usuario.username)

    #for comentario in comentarios:
        #comments.append(comentario)
    return jsonify({'participantes': participantes})


@bp.route('/get_group_comment', methods=('GET', 'POST'))
def get_group_comment():
    content = json.loads(request.data)
    grupo = db.session.query(Grupo).filter(Grupo.id_grupo == int(content['data'])).one()
    usuarios = grupo.usuarios
    comentarios = grupo.comentarios
    comments = []
    fecha = []
    usuario = []


    for comentario in comentarios:
        comments.append(comentario.comentario)
        fecha.append(comentario.fecha)
        usuario.append(comentario.categoria.usuario.username)


    return jsonify({'comments': comments,'fecha': fecha,'usuario': usuario})



def get_user_categories(user):
    return db.session.query(Categoria).filter(Categoria.id_usuario == user.id_usuario).all()


