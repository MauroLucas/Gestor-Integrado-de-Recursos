from flaskr.base import db
from flaskr.base import Etiqueta


#Agregar
#etiqueta = Etiqueta(nombre='python2')
#db.session.add(etiqueta)
#db.session.commit()
etiqueta1 = db.session.query(Etiqueta).filter(Etiqueta.id_etiqueta == 1).one()

#recuros de esa etiqueta

for recurso in etiqueta1.recursos:
    print recurso.recurso.recurso

