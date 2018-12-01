from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Kritchat',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'Dec 1, 2018'
    },
    {
        'author': 'Bang earl',
        'title': 'Blog Post2',
        'content': 'First post content',
        'date_posted': 'Dec 2, 2018'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

