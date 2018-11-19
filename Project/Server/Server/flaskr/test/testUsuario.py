from flaskr.base import db
from flaskr.base import Usuario,Categoria,Grupo

#AgregarUsuario
#usuario = Usuario(username='Mauro',password='1234',nombre='mauro',apellido='pereyra',mail='m_l_pereyra')
#db.session.add(usuario)
#db.session.commit()

#Traer grupos personales
usuario1 = db.session.query(Usuario).filter(Usuario.username == 'Mauro').one()
grupo1 = db.session.query(Grupo).filter(Grupo.id_grupo == 3).one()
print 'mis grupos:'

for grupo in usuario1.misGrupos:
    print grupo.nombre

#traer categorias
print 'categorias:'
for categoria in usuario1.categorias:
    print categoria.nombre


#agregar categoria a usuario
print'Grupos donde soy participante:'
for grupos in usuario1.grupos:
    print grupos.grupo.nombre

#agregar grupo a usuario