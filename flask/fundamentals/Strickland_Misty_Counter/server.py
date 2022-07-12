from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "I have a secret"



@app.route('/')
def counter():


    if 'counts' in session:
        session['counts'] += 1
        print('key exists!')
    else:
        session['counts'] = 1
        print("key 'counts' does NOT exist")

    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()		# clears all keys

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)