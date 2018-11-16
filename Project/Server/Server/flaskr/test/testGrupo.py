from flaskr.base import db
from flaskr.base import Usuario,Grupo

usuario = db.session.query(Usuario).filter(Usuario.username == 'Mauro').one()

grupo = Grupo(nombre='Mas bien loquita',id_admin=usuario.id_usuario)
db.session.add(grupo)
db.session.commit()