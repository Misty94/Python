from flask_app import app
from flask import render_template, request, redirect, session, flash
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

    user_already_exists = User.get_one_by_email(request.form)
    if user_already_exists != False:
        flash("This email already exists!", "error_registration_email")
        return redirect('/')


    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)
    user_id = User.save(data)
    
    session['first_name'] = data['first_name']   # store useful info into session, so you can personalize the pages
    session['email'] = data['email']
    session['user_id'] = user_id
    
    return redirect("/welcome")


@app.route('/login/user', methods=['POST'])
def process_login():
    
    current_user = User.get_one_by_email(request.form)
    if current_user == False:
        flash("Wrong email", "error_login_email")
        return redirect('/')
    if current_user != False:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Wrong password", "error_login_password")
            return redirect('/')
        else:
            session['first_name'] = current_user.first_name
            session['email'] = current_user.email
            session['user_id'] = current_user.id

            return redirect('/welcome')


@app.route('/welcome')
def welcome_page():

    if "email" not in session:
        return redirect('/')

    return render_template("welcome.html")


@app.route('/logout')
def process_logout():
    session.clear()
    return redirect('/')