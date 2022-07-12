from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Two can keep a secret if one of them is dead"


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process_form():
    print("Got Form Info")
    print(request.form)

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    # session['accept_emails'] = request.form['accept_emails']
    # session['very'] = request.form['very']
    # session['somewhat'] = request.form['somewhat']
    # session['ineffective'] = request.form['ineffective']

    return redirect('/results')


@app.route('/results')
def results():


    # submitted_form = {
    #     "name" : request.form['name'],
    #     'location' : request.form['location'],
    #     'language' : request.form['language'],
    #     'comment' : request.form['comment'],
    #     'accept_emails' : request.form['accept_emails'],
    #     'very' : request.form['very']
    # }
    

    return render_template("results.html", name=session['name'],location=session['location'],language=session['language'], comment=session['comment'])#, accept_emails=session['accept_emails'], very=session['very'], somewhat=session['somewhat'], ineffective=['ineffective'])



if __name__ == "__main__":
    app.run(debug=True)
