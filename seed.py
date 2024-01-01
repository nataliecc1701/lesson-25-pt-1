'''seeds file for the pet agency. includes little bunny foo-foo from the nursery rhyme'''

from app import app
from pet_models import Pet, db

# need to do this in the current version of SQLAlchemy
app.app_context().push()

db.drop_all()
db.create_all()

pets = [
    Pet(name="Foo-foo", species="Little Bunny", age=3, notes="In trouble with the good fairy")
]

db.session.add_all(pets)
db.session.commit()