import random
import requests
import json
from datetime import datetime
from flask import Flask, request, render_template

app = Flask("__name__")


@app.route("/")
def home():
    random_number = random.randint(1, 99)
    copyright_year = datetime.now().year
    copyright_name = "Hailey Kim"
    return render_template("index.html", num=random_number, year=copyright_year, name=copyright_name)


@app.route("/guess", methods=["GET", "POST"])
def guess():
    if request.method == "POST":
        name = request.form.get("name")
        return guess_by_name(name)
    return render_template("guess.html")


@app.route("/guess/<name>")
def guess_by_name(name):
    user_name = name.title()
    predicted_gender = requests.get(url=f"https://api.genderize.io?name={name}").json()["gender"]
    predicted_age = requests.get(url=f"https://api.agify.io?name={name}").json()["age"]
    return render_template("result.html", name=user_name, gender=predicted_gender, age=predicted_age)


@app.route("/blog")
def blog_posts():
    with open("blog-data.json") as file:
        data = json.load(file)["posts"]
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
