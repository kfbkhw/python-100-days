from post import Post
from flask import Flask, render_template

app = Flask(__name__)
post = Post()


@app.route('/blog')
def blog():
    return render_template("index.html", posts=post.data)


@app.route('/post/<post_id>')
def blog_post(post_id):
    data = post.find_post(post_id)
    return render_template("post.html", post=data)


if __name__ == "__main__":
    app.run(debug=True)
