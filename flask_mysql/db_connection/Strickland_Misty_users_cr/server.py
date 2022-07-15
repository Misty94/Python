from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route('/users')
def all_users():
    users = User.get_all()

    return render_template("read_all.html", users = users)


@app.route('/process_form', methods=['POST'])
def process():

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect('/users')
    

@app.route('/add/user')
def create_user():


    return render_template("create.html")




if __name__ == "__main__":
    app.run(debug=True)