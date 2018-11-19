from flaskr.base import db
from flaskr.base import Categoria,Usuario,Grupo,Comentario

grupo = db.session.query(Grupo).filter(Grupo.nombre=='grupo1').one()

#traer Comentarios

for comentario in grupo.comentarios:
    print comentario.comentario