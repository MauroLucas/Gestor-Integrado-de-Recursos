from flaskr.base import db
from flaskr.base import Grupo,Usuario

#usuario = db.session.query(Usuario).filter(Usuario.username == 'Mauro').one()

grupo = Grupo(nombre='Alto Vinito',id_admin=usuario.id_usuario)
db.session.add(grupo)
db.session.commit()

grupo1 = db.session.query(Grupo).filter(Grupo.id_grupo == 3).one()
usuario1 = db.session.query(Usuario).filter(Usuario.username == 'mauro1234').one()
#mostrar admin


#Mostras usuarios
for usuarios in grupo1.usuarios:
     print usuarios.usuario.nombre


#Agregar usuario a grupo
grupo1.usuarios.append(usuario1)
#db.session.commit()