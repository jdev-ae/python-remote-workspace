from flask import Flask, render_template

import test_data

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=test_data.posts, title='My Posts')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/health")
def health():
    return "Working fine"


if __name__ == '__main__':
    app.run(debug=True)
