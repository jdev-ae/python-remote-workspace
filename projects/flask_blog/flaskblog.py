from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import test_data
from blog_forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '6d0e21d41cbc2309e3656ab929ad21f2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_dev.db'

db = SQLAlchemy(app)


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
