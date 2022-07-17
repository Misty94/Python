from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo

@app.route('/dojos')
def all_dojos():

    dojos = Dojo.get_all()
    
    return render_template("all_dojos.html", dojos = dojos)


@app.route('/new_dojo', methods=['POST'])
def adding_new_dojo():

    data = {
        "name": request.form["name"]
    }

    Dojo.save(data)

    return redirect('/dojos')