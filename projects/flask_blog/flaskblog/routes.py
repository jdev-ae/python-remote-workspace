import os
import secrets

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from flaskblog import app, bcrypt, db
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User

from PIL import Image

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
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', title='Login', form=form)


def save_avatar(avatar):
    random_hex = secrets.token_hex(16)
    f_name, f_ext = os.path.splitext(avatar.filename)
    f_name = random_hex + f_ext
    local_path = os.path.join(app.root_path, 'static/profile_images', f_name)

    output_image_size = (200, 200)
    i = Image.open(avatar)
    i = i.convert('RGB')
    i.thumbnail(output_image_size)
    i.save(local_path)

    return f_name


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.avatar.data:
            f_name = save_avatar(form.avatar.data)
            current_user.avatar = f_name
        db.session.commit()

        flash('Account details has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    avatar = url_for('static', filename=f'profile_images/{current_user.avatar}')
    return render_template('account.html', title='Account', avatar=avatar, form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
