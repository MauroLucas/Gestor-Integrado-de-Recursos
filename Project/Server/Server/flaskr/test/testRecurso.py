from flaskr.base import db
from flaskr.base import Categoria,Recurso
import datetime

#recurso = Recurso(recurso='http://',descripcion='Paginaredsocial',fecha=datetime.datetime.now())

#db.session.add(recurso)
#db.session.commit()
recurso1 = db.session.query(Recurso).filter(Recurso.id_recurso == 2).one()
#Traer todas las categorias de ese recurso
print'categorias del recurso'
for cate in recurso1.categorias:
    print cate.categoria.nombre
print 'etiquetas del recurso'
for etiqueta in recurso1.etiquetas:
    print etiqueta.etiqueta.nombre
