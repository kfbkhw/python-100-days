from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def render_html_static_files():
    return render_template("cv/index.html")


@app.route("/0")
def render_html_css():
    return render_template("index.html")


@app.route("/00")
def render_personal_site():
    return render_template("personal-site/index.html")


@app.route("/index")
def render_downloaded_site_index():
    return render_template("html5up-massively/index.html")


@app.route("/generic")
def render_downloaded_site_generic():
    return render_template("html5up-massively/generic.html")


@app.route("/elements")
def render_downloaded_site_elements():
    return render_template("html5up-massively/elements.html")


if __name__ == "__main__":
    app.run(debug=True)
