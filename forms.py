'''forms for the pet agency'''

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField

class AddPetForm(FlaskForm):
    '''form to add pets'''
    name = StringField("Name of Pet")
    species = StringField("Species")
    photo_url = StringField("Photo of pet (URL)")
    age = IntegerField("Age (full years)")
    notes = StringField("Notes")
    