from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is the first webpage I\'ve created using Flask.</p>' \
           '<img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" width="400">'


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def good_bye():
    return "Bye!"


@app.route("/user/<name>/<int:number>")
def greeting(name, number):
    return f"<p>Hello, {name}! Your number is {number}.</p>"


if __name__ == "__main__":
    app.run(debug=True)
