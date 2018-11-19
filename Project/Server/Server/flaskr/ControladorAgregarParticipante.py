from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time
import datetime

urlAgregarParticipante = Blueprint('ControladorAgregarParticipante', __name__, url_prefix='/ControladorAgregarParticipante')


@urlAgregarParticipante.route('/agregar_participante', methods=('GET', 'POST'))
def agregar_participante():
    if request.method == 'POST':
        grupo= request.form['grupo']
        participante = request.form['participante']

        error = None
        if not grupo:
            error = 'Grupo is required.'
        if not participante:
            error = 'The group needs the participant'
        if error is None:
            #user = db.session.query(Usuario).filter(Usuario.username == session['user']).one()
            #recurso = Recurso(recurso=resource, descripcion=description, fecha=datetime.datetime.now())
            #db.session.add(recurso)
            #db.session.flush()
            #if db.session.query(Categoria.query.filter(Categoria.nombre == category).exists()).scalar():
             #   categoria = db.session.query(Categoria).filter(Categoria.nombre == category).one()
            #else:
             #   categoria = Categoria(nombre=category, id_usuario=user.id_usuario)
              #  db.session.add(categoria)
               # db.session.flush()
            #db.session.add(CategoriaXRecurso(id_recurso=recurso.id_recurso, id_categoria=categoria.id_categoria))
            #db.session.commit()
            print 'Participante ' +str(participante)
            print 'grupo ' +str(grupo)
            return redirect(url_for('auth.login_succesful'))

        flash(error)
    return render_template('agregarParticipante.html',grupos = (db.session.query(Usuario).filter(Usuario.username == session['user']).one()).grupos)


def get_user_categories(user):
    return db.session.query(Categoria).filter(Categoria.id_usuario == user.id_usuario).all()