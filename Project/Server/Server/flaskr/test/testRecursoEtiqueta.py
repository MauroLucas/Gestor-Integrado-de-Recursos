from flaskr.base import db
from flaskr.base import Recurso, RecursoXEtiqueta, Etiqueta


etiqueta = db.session.query(Etiqueta).filter(Etiqueta.id_etiqueta == 1).one()
print'Nombre Etiqueta'
print etiqueta.nombre

print'recursos por etiqueta'
for etique in etiqueta.recursos:
    print 'Recurso ' + str(etique.recurso.recurso)


