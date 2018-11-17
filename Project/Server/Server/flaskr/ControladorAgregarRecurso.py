from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time
import datetime
import re

urlAgregarRecurso = Blueprint('ControladorAgregarRecurso', __name__, url_prefix='/ControladorAgregarRecurso')


@urlAgregarRecurso.route('/enter_resource', methods=('GET', 'POST'))
def enter_resource():
    if request.method == 'POST':
        resource = request.form['resource']
        description = request.form['description']
        etiquetas = request.form['tags']
        if request.form['category_selection'] == 'nueva_categoria':
            category = request.form['category_input']
        else:
            category = request.form['category_selection']
        error = None
        if not resource:
            error = 'Resource is required.'
        if not category:
            error = 'The resource needs category'
        if error is None:
            user = db.session.query(Usuario).filter(Usuario.username == session['user']).one()
            recurso = Recurso(recurso=resource, descripcion=description, fecha=datetime.datetime.now())
            db.session.add(recurso)
            db.session.flush()
            if db.session.query(Categoria.query.filter(Categoria.nombre == category).exists()).scalar():
                categoria = db.session.query(Categoria).filter(Categoria.nombre == category).one()
            else:
                categoria = Categoria(nombre=category, id_usuario=user.id_usuario)
                db.session.add(categoria)
                db.session.flush()
            db.session.add(CategoriaXRecurso(id_recurso=recurso.id_recurso, id_categoria=categoria.id_categoria))
            if etiquetas:
                pattern = re.compile("^\s+|\s*,\s*|\s+$")
                etiquetas = [x for x in pattern.split(etiquetas) if x]
                for tag in etiquetas:
                    if db.session.query(Etiqueta.query.filter(Etiqueta.nombre == tag).exists()).scalar():
                        etiqueta = db.session.query(Etiqueta).filter(Etiqueta.nombre == tag).one()
                    else:
                        etiqueta = Etiqueta(nombre=tag)
                        db.session.add(etiqueta)
                        db.session.flush()
                    db.session.add(RecursoXEtiqueta(id_etiqueta=etiqueta.id_etiqueta, id_recurso=recurso.id_recurso))
            db.session.commit()
            return redirect(url_for('auth.login_succesful'))
        flash(error)
    return render_template('agregarRecurso.html', categorias=get_user_categories(db.session.query(Usuario).filter(Usuario.username == session['user']).one()))


def get_user_categories(user):
    return db.session.query(Categoria).filter(Categoria.id_usuario == user.id_usuario).all()
