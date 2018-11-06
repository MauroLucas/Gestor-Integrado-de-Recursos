from base import db
from base import Usuario

db.create_all()

admin = Usuario(username='franco', password='789456')

db.session.add(admin)
db.session.commit()
Usuario.query.all()
