'''forms for the pet agency'''

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

allowed_species = ["Cat", "Dog", "Porcupine"]

class AddPetForm(FlaskForm):
    '''form to add pets'''
    name = StringField("Name of Pet", validators=[InputRequired()])
    species = StringField("Species", validators=[AnyOf(allowed_species)])
    photo_url = StringField("Photo of pet (URL)", validators=[Optional(), URL()])
    age = IntegerField("Age (full years)", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    '''form to edit pets'''
    photo_url = StringField("Photo of pet (URL)", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available for Adoption")