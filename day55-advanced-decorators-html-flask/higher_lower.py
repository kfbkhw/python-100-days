from flask import Flask
from random import randint

app = Flask(__name__)
answer = 0
result = None


@app.route("/")
def home():
    global answer
    answer = randint(0, 9)
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<center><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></center>"


@app.route("/<int:guess>")
def check(guess):
    global answer, result
    if guess > answer:
        result = "<h1 style='text-align: center'>Too high, try again!</h1>" \
                 "<center><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></center>"
    elif guess < answer:
        result = "<h1 style='text-align: center'>Too low, try again!</h1>" \
                 "<center><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></center>"
    else:
        result = "<h1 style='text-align: center'>You found me!</h1>" \
                 "<center><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></center>"
    return result


if __name__ == "__main__":
    app.run()
