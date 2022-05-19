#The backbone of the flask app
#all other pieces of the flask app must connect back to this file
# and this file is the hub of all communication between independent pieces of the flask app

#from the flask package import the Flask object/class
#if flask has squiggly marks under it, select the interpreter for this virtual environment
#To do this, click the interpreter in the bottom right. As of recent, it is to the left of the Go Live button on the blue bar at the bottom
# And it is to the right of the Python name in the blue bar
from flask import Flask
# from the config file import the config class that we created
from config import Config

#define/instantiate our flask app... aka create the actual object that will be our Flask app
app = Flask(__name__)

# tell this app how it is going to be configured
app.config.from_object(Config)
# aka configuring our flask app based on the Config class we made in the config.py file

# our flask app is really dumb. if we do not tell it about the existence of other files, it will assume they do not exist
#import the routes file here so that our Flask app knows the routes exist
#this is one of the only scenarios where imports will be at the bottom of a file 
    # these imports must be after the instantiation of the flask app and the configuration
from . import routes # from the app folder(this folder), import the entire routes file