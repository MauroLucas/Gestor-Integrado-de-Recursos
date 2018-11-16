from flaskr.base import db
from flaskr.base import Etiqueta


#Agregar
etiqueta = Etiqueta(nombre='python2')
db.session.add(etiqueta)
db.session.commit()

