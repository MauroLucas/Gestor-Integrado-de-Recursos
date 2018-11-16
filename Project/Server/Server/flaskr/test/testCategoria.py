from flaskr.base import db
from flaskr.base import Categoria,Usuario
#Agregar categoria a un usuario
usuario = db.session.query(Usuario).filter(Usuario.username == 'Mauro').one()

categoria = Categoria(id_usuario=usuario.id_usuario,nombre='Desarrollo de Videojuegos')
db.session.add(categoria)
db.session.commit()