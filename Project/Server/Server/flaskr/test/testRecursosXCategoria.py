from flaskr.base import db
from flaskr.base import Recurso, RecursoXEtiqueta, Etiqueta, Usuario, Categoria, CategoriaXRecurso
from flask import session

categoria= db.session.query(Categoria).filter(Categoria.id_categoria == 1).one()

print'Nombre Categoria'
print categoria.nombre

print'recursos por categoria'
for categoria in categoria.recursos:
    print 'Recurso ' + str(categoria.recurso.recurso)