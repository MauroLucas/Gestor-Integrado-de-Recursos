from flaskr.base import db
from flaskr.base import Categoria,Usuario
#Agregar categoria a un usuario
#usuario = db.session.query(Usuario).filter(Usuario.username == 'Mauro').one()

#categoria = Categoria(id_usuario=usuario.id_usuario,nombre='Desarrollo de Videojuegos')
#db.session.add(categoria)
#db.session.commit()

#traer usuario de esa categoria
categoria = db.session.query(Categoria).filter(Categoria.id_categoria == 1).one()
print'Duenio categoria:'
print categoria.usuario.nombre

print'recursos de esa categoria'
for cate in categoria.recursos:
    print 'Recurso ' + str(cate.recurso.recurso)
    print 'etiquetas:'
    for etiqueta in cate.recurso.etiquetas:
        print ' ' + str(etiqueta.etiqueta.nombre)