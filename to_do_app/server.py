from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"

# @app.route( '/') # must go above the if statement
# @app.route( '/login' ) # both of these (if added to URL) will take you to the same place
# def hello_world():
#     return "Hello Python July 2022 class!"


# just add /python to your URL
# @app.route( '/python' )
# def display_python_message():
#     return "Hello, this is a different route /python."

# @app.route( '/hello/<first_name>/<last_name>' ) # this will grab the variable name (like a placeholder) // u can type the name in the browers there
# def greet_person( first_name, last_name ): # whatever is in the above < > needs to be the parameter also
    # print(f"Hey there {first_name} {last_name}")
    # return f"Howdy, {first_name} {last_name}"

# if there is a syntax error, the server/browser will shut down & you have to run the server again (python server.py)

# @app.route('/info/<name>/<int: age>')
# def display_info(name, age):
#     print(type(name), type(age))
#     return f"Name: {name} Age: {age}"

list_of_users = [{
    "first_name" : "Alex",
    "last_name" : "Miller",
    "id" : 1
},
{
    "first_name" : "Martha",
    "last_name" : "Smith",
    "id" : 2
},
{
    "first_name" : "Kenia",
    "last_name" : "Riveria",
    "id" : 3
}]

list_of_todos = [{
    "description" : "Learn Python",
    "status": "complete",
    "id" : 1,
    "user_id" : 1
},
{
    "description" : "Learn OOP",
    "status": "in_progress",
    "id" : 2,
    "user_id" : 1
},
{
    "description" : "Learn routes in Flask",
    "status": "in_progress",
    "id" : 3,
    "user_id" : 2
},
{
    "description" : "Learn POST",
    "status": "in_progress",
    "id" : 4,
    "user_id" : 3
}
]

"""
Method: GET
Getting all of a particular type
URL: '/todos'
Function: get_all_todos
        get_todos()

Method: GET
Getting one of a particular type
URL: '/todo/<int:id>'
Function: get_todo_by_id( id )

Method: GET
Displaying a form for a type
URL: '/todo/form'
Function: display_todo_form()

Method: POST
Creating a new type
URL: '/todo/new


"""


@app.route( "/todos")
def get_todos():
    return render_template("todos.html", todos = list_of_todos)

@app.route('/todo/form')
def display_todo_form():
    return render_template('todo_form.html', users = list_of_users)

@app.route('/todo/new', methods=['POST'])
def create_todo():
    # print(request.form)
    new_todo = {
        "id" : int(request.form['id']),
        "description" : request.form['description'],
        "status" : request.form['status'],
        "user_id" : int(request.form['user_id'])
    }
    list_of_todos.append(new_todo)
    return redirect('/todos')




if __name__=="__main__": #Ensure this file is being run directly and not from a different module
    app.run(debug=True) # run the app in debug mode