from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *

urlCrearGrupo = Blueprint('ControladorCrearGrupo', __name__, url_prefix='/ControladorCrearGrupo')


@urlCrearGrupo.route('/crear_grupo', methods=('GET', 'POST'))
def crear_grupo():
    if request.method == 'POST':
        grupo = request.form['grupo']


        error = None
        if not grupo:
            error = 'Grupo is required.'

        if error is None:
            user = db.session.query(Usuario).filter(Usuario.username == session['user']).one()
            grupo1 = Grupo(nombre=grupo, id_admin=user.id_usuario)
            db.session.add(grupo1)
            #db.session.flush()
            #if db.session.query(Categoria.query.filter(Categoria.nombre == category).exists()).scalar():
                #categoria = db.session.query(Categoria).filter(Categoria.nombre == category).one()
           # else:
                #categoria = Categoria(nombre=category, id_usuario=user.id_usuario)
                #db.session.add(categoria)
                #db.session.flush()
            #db.session.add(CategoriaXRecurso(id_recurso=recurso.id_recurso, id_categoria=categoria.id_categoria))
            db.session.commit()
            return redirect(url_for('auth.login_succesful'))
        flash(error)
    return render_template('agregarGrupo.html')


def get_user_categories(user):
    return db.session.query(Categoria).filter(Categoria.id_usuario == user.id_usuario).all()
