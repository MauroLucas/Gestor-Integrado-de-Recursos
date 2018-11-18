from flaskr.base import db
from flaskr.base import Categoria,Usuario,Etiqueta


usuario = db.session.query(Usuario).filter(Usuario.username == 'Mauro').one()
etiqueta1 = db.session.query(Etiqueta).filter(Etiqueta.nombre == 'cumbia').one()

print etiqueta1.id_etiqueta

recursosEnEtiqueta = []

for categoria in usuario.categorias:
    print 'Categoria ' + str(categoria.nombre)
    for recurso in categoria.recursos:
        print ' Recurso ' + str(recurso.recurso.recurso)
        for etiqueta in recurso.recurso.etiquetas:
            print '  Etiqueta ' + str(etiqueta.etiqueta.nombre)
            if etiqueta.etiqueta.id_etiqueta==etiqueta1.id_etiqueta:
                recursosEnEtiqueta.append(recurso.recurso)

print 'Mis re cursos de la etiqeuta ' + str(etiqueta1.nombre)
for recu in recursosEnEtiqueta:
    print recu.recurso

