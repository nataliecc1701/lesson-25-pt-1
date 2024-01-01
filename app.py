'''Main App'''

# Flask imports
from flask import Flask, render_template, redirect, request

# local imports
from models import connect_db, Pet

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

@app.route("/add", methods=["GET, POST"])
def add_pet():
    return render_template("add-pet.html")