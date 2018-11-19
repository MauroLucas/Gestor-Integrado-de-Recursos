from flaskr.base import db
from flaskr.base import Recurso, Comentario

comentario1 = db.session.query(Comentario).filter(Comentario.id_comentario == 1).one()

print 'grupo '
print comentario1.grupo.nombre
print 'Categoria ' + str(comentario1.categoria.nombre)
print 'recuros de esa categoria : '
for recuro in comentario1.categoria.recursos:
    print recuro.recurso.recurso
print('Recursos Compartidos ')
for recurso in comentario1.recursos:
    print recurso.recurso.recurso
