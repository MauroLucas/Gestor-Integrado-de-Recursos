from base import db
from base import User

db.create_all()

admin = User(username='gian_nativo', password='123456')

db.session.add(admin)
db.session.commit()

User.query.all()
