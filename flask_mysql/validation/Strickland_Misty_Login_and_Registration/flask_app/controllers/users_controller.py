from flask_app import app
from flask import render_template
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


@app.route('/')
def login_and_registration():

    return render_template("login.html")