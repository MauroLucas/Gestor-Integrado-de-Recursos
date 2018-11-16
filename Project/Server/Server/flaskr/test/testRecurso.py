from flaskr.base import db
from flaskr.base import Categoria,Recurso
import datetime

recurso = Recurso(recurso='http://',descripcion='Paginaredsocial',fecha=datetime.datetime.now())

db.session.add(recurso)
db.session.commit()