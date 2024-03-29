'''Main App'''

import sys
print(sys.path)

# Flask imports
from flask import Flask, render_template, redirect, flash, request

# local imports
from forms import AddPetForm, EditPetForm
from models import connect_db, db, Pet

app = Flask(__name__)

# pull our config parameters from a text file
with open("config.txt") as config:
    for line in config:
        params=line.split()
        
        # parse string to bools
        if params[1] == "True":
            params[1] = True
        elif params[1] == "False":
            params[1] = False
        
        # apply to app.config
        app.config[params[0]] = params[1]
        
connect_db(app)


# routes
@app.route("/")
def show_all_pets():
    '''Shows the index page, listing all pets'''
    pets = Pet.query.all()
    return render_template("all-pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    '''Shows and receives the add pet form'''
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"New pet added: {name}")
        return redirect("/")
    else:
        return render_template("add-pet.html", form=form)
    
@app.route("/<int:pet_ID>", methods = ["GET", "POST"])
def show_pet_details(pet_ID):
    '''Route for things specific to each pet (details and update form)'''
    pet = Pet.query.get_or_404(pet_ID)
    form = EditPetForm(obj = pet)
    
    if form.validate_on_submit():
        # update the pet
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        # send to the database
        db.session.add(pet)
        db.session.commit()
        
        flash(f"{pet.name} updated successfully")
        return redirect("/")
    else:
        return render_template("pet-info.html", pet=pet, form=form)