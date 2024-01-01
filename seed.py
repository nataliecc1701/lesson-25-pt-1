from app import app
from models import Pet, db

# need to do this in the current version of SQLAlchemy
app.app_context().push()

db.drop_all()
db.create_all()

pets = [
    Pet(name="Foo-foo", species="Little Bunny", age=3, notes="In trouble with the good fairy")
]

db.session.add_all(pets)
db.session.commit()