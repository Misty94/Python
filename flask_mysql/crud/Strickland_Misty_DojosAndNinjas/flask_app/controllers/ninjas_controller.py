from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import ninja_model, dojo_model

@app.route('/ninjas')
def new_ninja():

    dojos = dojo_model.Dojo.get_all()


    return render_template("new_ninja.html", dojos = dojos)

@app.route('/new_ninja', methods=['POST'])
def adding_new_ninja():

    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }

    ninja_model.Ninja.save(data)

    data_id = data['dojo_id']

    return redirect(f'/dojos/{data_id}')