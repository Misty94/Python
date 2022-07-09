from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)  


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():

    height = 200
    num_of_hellos = 10
    student_info = [
        {"name" : "Misty", "age": 28},
        {"name": "Elena", "age": 22},
        {"name": "Joe", "age": 59},
        {"name": "Jenna", "age": 30}
    ]

    return render_template("index.html",times=num_of_hellos, list=student_info, height=height) 



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 