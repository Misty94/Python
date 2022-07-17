from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def new_ninja():


    return render_template("new_ninja.html")

@app.route('/new_ninja')
def adding_new_ninja():

    data = {
        "dojo": request.form['dojo'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }

    Ninja.save(data)

    return redirect('/ninjas')