from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def rendering_html_static_files():
    return render_template("cv/index.html")


@app.route("/0")
def rendering_html_css():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
