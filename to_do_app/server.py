from flask import Flask # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"

@app.route( '/') # must go above the if statement
@app.route( '/login' ) # both of these (if added to URL) will take you to the same place
def hello_world():
    return "Hello Python July 2022 class!"


# just add /python to your URL
@app.route( '/python' )
def display_python_message():
    return "Hello, this is a different route /python."

@app.route( '/hello/<first_name>/<last_name>' ) # this will grab the variable name (like a placeholder) // u can type the name in the browers there
def greet_person( first_name, last_name ): # whatever is in the above < > needs to be the parameter also
    print(f"Hey there {first_name} {last_name}")
    return f"Howdy, {first_name} {last_name}"

# if there is a syntax error, the server/browser will shut down & you have to run the server again (python server.py)

@app.route('/info/<name>/<int: age>')
def display_info(name, age):
    print(type(name), type(age))
    return f"Name: {name} Age: {age}"



if __name__=="__main__": #Ensure this file is being run directly and not from a different module
    app.run(debug=True) # run the app in debug mode