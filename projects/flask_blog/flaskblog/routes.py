from flask import render_template, flash, redirect, url_for
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app

test_posts = [
    {
        'author': 'Surendra',
        'title': 'The first post',
        'content': 'This is the first post',
        'date_posted': 'June 26, 2019'
    },
    {
        'author': 'Surendra',
        'title': 'Welcome',
        'content': 'The flask demo app',
        'date_posted': 'June 27, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=test_posts, title='My Posts')


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
