from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *

urlAgregarRecurso = Blueprint('ControladorAgregarRecurso', __name__, url_prefix='/ControladorAgregarRecurso')

@urlAgregarRecurso.route('/enter_resource', methods=('GET', 'POST'))
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
    return render_template('agregarRecurso.html')