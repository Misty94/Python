from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
            
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # print(request.form)
    # name = request.form['name']
    # email = request.form['email']
    return redirect("/show")	 
    

# adding this method
@app.route("/show")
def show_user():
    # print("Showing the User Info From the Form")
    # print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=['useremail'])




if __name__ == "__main__":
    app.run(debug=True)

