from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checkerboard1():
    num_of_rows = 8
    col = 8

    return render_template("index.html", times=num_of_rows, col=col)

@app.route('/<x>')
def small_checkerboard(x):
    row = int(x)
    col = 8


    return render_template("index.html", times=row, col=col)

@app.route('/<x>/<y>')
def row_and_col(x, y):
    row = int(x)
    col = int(y)

    return render_template("index.html", times=row, col=col)

# @app.route('/<x>/<y>/<color1>/<color2>')
# def colors(x, y, color1, color2):
#     row = int(x)
#     col = int(y)
#     color1 = color1
#     color2 = color2

#     return render_template("index.html", times=row, col=col, color1=color1, color2=color2)



if __name__=="__main__":
    app.run(debug=True)