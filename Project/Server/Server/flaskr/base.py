from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/gir'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave_secreta'
db = SQLAlchemy(app)


class Contacto(db.Model):
    __tablename__ = 'Contacto'
    # Primary key
    id_contacto = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_contactos = db.relationship('DatosUsuario', backref='DatosUsuario.id_datosUsuario',
                                   primaryjoin='DatosUsuario.id_contacto==Contacto.id_contacto')
    # Atributtes
    movil = db.Column(db.String(80), unique=False, nullable=False)
    fijo = db.Column(db.String(80), unique=False, nullable=False)
    calle = db.Column(db.String(80), unique=False, nullable=False)
    numero = db.Column(db.String(80), unique=False, nullable=False)


class DatosUsuario(db.Model):
    __tablename__ = 'DatosUsuario'
    # Primary key
    id_datosUsuario = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_contacto = db.Column(db.Integer, db.ForeignKey('Contacto.id_contacto'), nullable=True)
    # Relationship
    id_datosUsuarios = db.relationship('Usuario', backref='Usuario.id_datosUsuario',
                                       primaryjoin='Usuario.id_datosUsuario==DatosUsuario.id_datosUsuario')
    # Atributtes
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    apellido = db.Column(db.String(80), unique=False, nullable=False)
    mail = db.Column(db.String(80), unique=False, nullable=False)


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    # Primary key
    id_usuario = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_datosUsuario = db.Column(db.Integer, db.ForeignKey('DatosUsuario.id_datosUsuario'), nullable=True)
    # Relationship
    id_usuarios_ = db.relationship('UsuarioXGrupo', backref='UsuarioXGrupo.id_usuario',
                                   primaryjoin='Usuario.id_usuario==UsuarioXGrupo.id_usuario')
    id_usuarios = db.relationship('Grupo')
    id_usuarios_categoria = db.relationship('Categoria')
    # Atributtes
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class UsuarioXGrupo(db.Model):
    __tablename__ = 'UsuarioXGrupo'
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=True)
    id_grupo = db.Column(db.Integer, db.ForeignKey('Grupo.id_grupo'), nullable=True)


class Grupo(db.Model):
    __tablename__ = 'Grupo'
    # Primary key
    id_grupo = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_admin = db.Column(db.Integer, db.ForeignKey(Usuario.id_usuario), nullable=True)
    # Relationship
    id_grupos_ = db.relationship('UsuarioXGrupo', backref='UsuarioXGrupo.id_grupo',
                                 primaryjoin='Grupo.id_grupo==UsuarioXGrupo.id_grupo')
    id_grupos = db.relationship('Comentario', backref='Cometario.id_comentario',
                                primaryjoin='Grupo.id_grupo==Comentario.id_grupo')
    # Atributtes
    nombre = db.Column(db.String(80), unique=False, nullable=False)


class Comentario(db.Model):
    __tablename__ = 'Comentario'
    # Primary key
    id_comentario = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_grupo = db.Column(db.Integer, db.ForeignKey(Grupo.id_grupo), nullable=True)
    # Atributtes
    comentario = db.Column(db.String(80), unique=False, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)


class Etiqueta(db.Model):
    __tablename__ = 'Etiqueta'
    # Primary key
    id_etiqueta = db.Column(db.Integer, primary_key=True)
    # Atributte
    nombre = db.Column(db.String(80), unique=False, nullable=True)
    # relationship
    id_etiquetas = db.relationship('RecursoXEtiqueta')


class RecursoXEtiqueta(db.Model):
    __tablename__ = 'RecursoXEtiqueta'
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_recurso = db.Column(db.Integer, db.ForeignKey('Recurso.id_recurso'), nullable=True)
    id_etiqueta = db.Column(db.Integer, db.ForeignKey('Etiqueta.id_etiqueta'), nullable=True)


class Recurso(db.Model):
    __tablename__ = 'Recurso'
    # Primary key
    id_recurso = db.Column(db.Integer, primary_key=True)
    # Relationship
    id_recursos = db.relationship('RecursoXEtiqueta')
    id_recursos_ = db.relationship('CategoriaXRecurso')
    # Atributtes
    recurso = db.Column(db.String(80), unique=False, nullable=True)
    descripcion = db.Column(db.String(80), unique=False, nullable=False)


class CategoriaXRecurso(db.Model):
    __tablename__ = 'CategoriaXRecurso'
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_categoria = db.Column(db.Integer, db.ForeignKey('Categoria.id_categoria'), nullable=True)
    id_recurso = db.Column(db.Integer, db.ForeignKey('Recurso.id_recurso'), nullable=True)


class Categoria(db.Model):
    __tablename__ = 'Categoria'
    # Primary key
    id_categoria = db.Column(db.Integer, primary_key=True)
    # Foreign key
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=True)
    # Relationship
    id_categorias_ = db.relationship('CategoriaXRecurso')
    # Atributtes
    nombre = db.Column(db.String(80), unique=False, nullable=False)


# INSERTS-----------
contact = Contacto(movil='1155447788', fijo='41231234', calle='Tacuario', numero='3321')
date = DatosUsuario(id_contacto=6, nombre='lucas', apellido='ambesi', mail='lucasambesi@hotmail.com')
admin = Usuario(id_datosUsuario='2', username='lucas', password='12345')
group = Grupo(nombre='grupo1', id_admin=4)
integrante = UsuarioXGrupo(id_usuario=5, id_grupo=9)
comment = Comentario(comentario='link1 + comentario1', id_grupo=9)
label = Etiqueta(nombre='python')
category = Categoria(id_usuario=4, nombre='Python')
resource = Recurso(recurso='http://flask.pocoo.org/', descripcion='Micro-framework para desarrollo web en python')
recursos = CategoriaXRecurso(id_categoria=1, id_recurso=1)
etiquetas = RecursoXEtiqueta(id_etiqueta=1, id_recurso=1)
'''
db.session.add(contact)
db.session.commit()
Contacto.query.all()

db.session.add(date)
db.session.commit()
DatosUsuario.query.all()

db.session.add(admin)
db.session.commit()
Usuario.query.all()

db.session.add(group)
db.session.commit()
Grupo.query.all()

db.session.add(integrante)
db.session.commit()
UsuarioXGrupo.query.all()

db.session.add(comment)
db.session.commit()
Comentario.query.all()

db.session.add(label)
db.session.commit()
Etiqueta.query.all()

db.session.add(category)
db.session.commit()
Categoria.query.all()

db.session.add(resource)
db.session.commit()
Recurso.query.all()

db.session.add(recursos)
db.session.commit()
CategoriaXRecurso.query.all()

db.session.add(etiquetas)
db.session.commit()
RecursoXEtiqueta.query.all()
'''
