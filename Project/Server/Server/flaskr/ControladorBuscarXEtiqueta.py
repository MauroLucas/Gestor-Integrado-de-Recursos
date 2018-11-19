from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time
import datetime

urlBuscarXEtiqueta = Blueprint('ControladorBuscarXEtiqueta', __name__, url_prefix='/ControladorBuscarXEtiqueta')

@urlBuscarXEtiqueta.route('/buscar_etiqueta', methods=('GET', 'POST'))
def buscar_etiqueta():
    if request.method == 'POST':
        etiqueta = request.form['etiquetabuscar']
        user = session["user"]
        recursosEnEtiqueta = []
        error = None
        if not etiqueta:
            error = 'Inserte etiqueta'
        if error is None:
            if db.session.query(Etiqueta.query.filter(Etiqueta.nombre == etiqueta).exists()).scalar():
                usuario = db.session.query(Usuario).filter(Usuario.username == user).one()
                etiqueta1 = db.session.query(Etiqueta).filter(Etiqueta.nombre == etiqueta).one()

                for categoria in usuario.categorias:
                    for recurso in categoria.recursos:
                        for etiqueta in recurso.recurso.etiquetas:
                            if etiqueta.etiqueta.id_etiqueta == etiqueta1.id_etiqueta:
                                recursosEnEtiqueta.append(recurso.recurso.recurso)
                return render_template('buscar_por_etiqueta.html', recursosBuscados=recursosEnEtiqueta)
        flash (error)
    return render_template ('buscar_por_etiqueta.html')


