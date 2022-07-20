from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def login_and_registration():

    return render_template("login.html")


@app.route('/register/user', methods=['POST'])
def process_registration():
    
    if User.validate_user(request.form) == False:
        return redirect('/')

    # pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # print(pw_hash)

    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }

    print(data)
    user_id = User.save(data)
    
    session['first_name'] = data['first_name']   # store useful info into session, so you can personalize the pages
    session['user_id'] = user_id
    
    return redirect("/")


@app.route('/process/login', methods=['POST'])
def process_login():
    pass