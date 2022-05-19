# flask routes control what content is shown on what url
    #depending on how the user is accessing the url (methods), what buttons they've pressed, or what requests they've made, what their permissions are, etc.

# the general structure of a flask rre is a function with a decorator
# the decorator adds another function/loines of code that run before and/or after the function being decorated

# our first route:
#just diplya 'hello world' on our localhost url (when we run a flasp app locally, it will default run on the following url)
    # http://127.0.0.1:5000/

#in order to set up a route we need a few tools
# 1. we need access to our Flask object
from app import app
#we need to be able to return an html file from our flask routes
#using render_template() from the flask package
from flask import render_template

import requests as r
# route decoor: 
# @<flask object/blueprint name>.route('/url endpoint', <methods>)
#followed by a regular python function
@app.route('/')
def home():
    #this is a regular python function, I can write normal python code here
    greeting = 'Hello, Foxes'
    print(greeting)
    students = ['Luke', 'Han', 'Leia', 'Chewy', 'R2-D2', 'C3P0', 'Lando']
    #the return value of this function is what is displayed on the webpage
    return render_template('index.html', g=greeting, students=students)


@app.route('/about')
def about():
    return render_template('about.html')


# advanced routing and python code
@app.route('/drivers')
def f1Drivers():
    #make api call and utilize info from api call in the HTML template
    #in order to make API call need requests package
    data = r.get('https://ergast.com/api/f1/current/driverStandings.json')
    if data.status_code == 200:
        data = data.json()
    return render_template('f1.html', data=data)

    #try:
        # hopint the API call goes well
    #except:
        # what to do if API call is broke