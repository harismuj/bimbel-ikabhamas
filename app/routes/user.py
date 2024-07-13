from flask import Blueprint, render_template, url_for, flash, redirect, request
import requests as req
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Layanan, Alumni, ProgramFasilitas, Keunggulan, Artikel, Visitor, Profil, SocialMediaLink
from app.forms import LoginForm, RegistrationForm

user = Blueprint('user', __name__)

def get_public_ip():
    response = req.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

def countVisitor():
    ip_address = get_public_ip()
    if not Visitor.query.filter_by(ip_address=ip_address).first():
        visitor = Visitor(ip_address=ip_address)
        db.session.add(visitor)
        db.session.commit()
        
@user.context_processor
def inject_data():
    profile = Profil.query.get_or_404(1)
    articles = Artikel.query.all()
    programs = ProgramFasilitas.query.all()
    socmedlink = SocialMediaLink.query.get_or_404(1)
    return dict(profile=profile, articles=articles, programs=programs, socmed=socmedlink)

@user.route("/")
@user.route("/home")
def home():
    countVisitor()
    return render_template('user/index.html',title='Home')

@user.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data,lastname=form.lastname.data,username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', title='Register', form=form)

@user.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('user/login.html', title='Login', form=form)

@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.home'))

@user.route("/layanan")
def layanan():
    services = Layanan.query.all()
    return render_template('user/layanan.html',title='Layanan', services=services)

@user.route("/alumni")
def alumni():
    alumni_list = Alumni.query.all()
    return render_template('user/alumni.html',title='Alumni' ,alumni_list=alumni_list)

@user.route("/program")
def program():
    programs = ProgramFasilitas.query.all()
    return render_template('user/program.html',title='Program', programs=programs)

@user.route("/keunggulan")
def keunggulan():
    keunggulan = Keunggulan.query.all()
    return render_template('user/keunggulan.html',title='Keunggulan', keunggulan=keunggulan)

@user.route("/artikel")
def artikel():
    articles = Artikel.query.all()
    return render_template('user/artikel.html',title='Artikel', articles=articles)


