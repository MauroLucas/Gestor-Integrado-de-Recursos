from flaskr.base import db
from flaskr.base import Categoria,Usuario,Etiqueta


usuario = db.session.query(Usuario).filter(Usuario.username == 'qwerty').one()
etiqueta1 = db.session.query(Etiqueta).filter(Etiqueta.nombre == 'python').one()

recursosEnEtiqueta = []
for categoria in usuario.categorias:
    for recurso in categoria.recursos:
        for etiqueta in recurso.recurso.etiquetas:
            if etiqueta.etiqueta.id_etiqueta==etiqueta1.id_etiqueta:
                recursosEnEtiqueta.append(recurso.recurso)

print 'Rcursos de la etiqueta ' + str(etiqueta1.nombre)
for recu in recursosEnEtiqueta:
    print recu.recurso

