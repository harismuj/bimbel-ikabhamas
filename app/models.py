from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
import pytz

timezone = pytz.timezone('Asia/Jakarta')
datetimeplus7 = datetime.now(timezone)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(30),nullable=True,default="user")

class Layanan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)

class Alumni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.Text)
    graduation_year = db.Column(db.Integer, nullable=False)
    current_position = db.Column(db.String(100), nullable=False)

class ProgramFasilitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Keunggulan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Artikel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    keyword = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetimeplus7)

class Profil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    alamat = db.Column(db.String(150), nullable=True)
    site_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    keyword = db.Column(db.Text)
    logo = db.Column(db.Text)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetimeplus7)

    def __repr__(self):
        return f'<Visitor {self.ip_address}>'
    
class Jasmani(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_siswa = db.Column(db.String(180), nullable=False)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    nilai_lari = db.Column(db.String(20), nullable=False)
    nilai_pullup = db.Column(db.String(20), nullable=True)
    nilai_situp = db.Column(db.String(20), nullable=False)
    nilai_pushup = db.Column(db.String(20), nullable=False)
    nilai_shutrun = db.Column(db.String(20), nullable=False)
    nilai_renang = db.Column(db.String(20), nullable=False)
    nilai_akhir = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetimeplus7)

class SocialMediaLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wa = db.Column(db.String(20), nullable=True)
    instagram = db.Column(db.String(250), nullable=True)
    tiktok = db.Column(db.String(250), nullable=True)

