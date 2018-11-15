from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/gir'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave_secreta'
db = SQLAlchemy(app)




class Usuario(db.Model):
    __tablename__ = 'Usuario'
    # Primary key
    id_usuario = db.Column(db.Integer, primary_key=True)


    # Relationship
    id_usuarios_ = db.relationship('UsuarioXGrupo', backref='UsuarioXGrupo.id_usuario',
                                   primaryjoin='Usuario.id_usuario==UsuarioXGrupo.id_usuario')
    id_usuarios = db.relationship('Grupo')
    id_usuarios_categoria = db.relationship('Categoria')
    # Atributtes
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(120), unique=False, nullable=False)
    nombre = db.Column(db.String(45), unique=False, nullable=False)
    apellido = db.Column(db.String(45), unique=False, nullable=False)
    mail = db.Column(db.String(45), unique=False, nullable=False)

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



