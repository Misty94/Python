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

    return redirect('/user/<int:id>')
    

@app.route('/add/user')
def create_user():


    return render_template("create.html")


@app.route('/user/<int:id>')
def show_user(id):

    data = {
        "id":id
    }

    user = User.get_one(data)

    return render_template("one.html", user = user)


@app.route('/user/edit/<int:id>')
def edit_user(id):

    data = {
        "id": id
    }

    user = User.get_one(data)


    return render_template("edit.html", user=user)

# @app.route('/process_update', methods = ['POST'])
# def edit_user():

#     data = {
#         "first_name": request.form['first_name'],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"],
#         "id": id
#     }

#     User.update_one(data)

#     return redirect('/users')

@app.route('/user/update/<int:id>', methods=['POST'])
def update_form(id):

    data = {
        "id": id,
        "first_name": request.form['first_name'],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }

    User.update_one(data)


    return redirect('/user/<int:id>')

@app.route('/user/delete/<int:id>')
def delete_user(id):
    
    data = {
        'id': id
    }

    User.delete_one(data)

    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)