from flaskr.base import db
from flaskr.base import Usuario

#AgregarUsuario
usuario = Usuario(username='Mauro',password='1234',nombre='mauro',apellido='pereyra',mail='m_l_pereyra')
db.session.add(usuario)
db.session.commit()

#Traer Categorias

