from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is the first webpage I\'ve created using Flask.</p>' \
           '<img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" width="400">'


@app.route("/bye")
def good_bye():
    return "<p>Bye!</p>"


@app.route("/user/<name>/<int:number>")
def greeting(name, number):
    return f"<p>Hello, {name}! Your number is {number}.</p>"


if __name__ == "__main__":
    app.run(debug=True)
