from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time

urlAgregarRecurso = Blueprint('ControladorAgregarRecurso', __name__, url_prefix='/ControladorAgregarRecurso')


@urlAgregarRecurso.route('/enter_resource', methods=('GET', 'POST'))
def enter_resource():
    if request.method == 'POST':
        resource = request.form['resource']
        description = request.form['description']
        category = request.form['catergory']
        error = None
        if not resource:
            error = 'Resource is required.'
        if not category:
            error = 'The resource needs category'
        if error is None:
            user = db.session.query(Usuario).filter(Usuario.username == session['user']).one()
            recurso = Recurso(recurso=resource, descripcion=description, fecha=time.clock())
            db.session.add(recurso)
            db.session.flush()
            if db.session.query(Categoria.query.filter(Categoria.nombre == category).exists()).scalar():
                categoria = db.session.query(Categoria).filter(Categoria.nombre == category).one()
                db.session.add(CategoriaXRecurso(db.session))
            else:
                db.session.add(Categoria(nombre=category, id_usuario=user.id_usuario))
            db.session.commit()
            return redirect(url_for('auth.login_succesful'))
        flash(error)
    return render_template('agregarRecurso.html')
