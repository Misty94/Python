from flask import Flask
app = Flask(__name__)
# app.secret_key = "It is my secret"


@app.route('/')
def index():

    return "hello"


if __name__ == "__main__":
    app.run(debug=True)