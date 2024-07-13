from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from app.models import User

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=60)])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=60)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username telah digunakan')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email telah digunakan')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    phone = StringField('Phone', validators=[Optional(), Length(max=20)])
    alamat = StringField('Address', validators=[Optional(), Length(max=150)])
    site_name = StringField('Site Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[Optional()])
    keyword = TextAreaField('Keyword', validators=[Optional()])
    logo = FileField('Logo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')

class JasmaniForm(FlaskForm):
    nama_siswa = StringField('Nama Siswa', validators=[DataRequired()])
    jenis_kelamin = SelectField('Jenis Kelamin', choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], validators=[DataRequired()])
    nilai_lari = FloatField('Nilai Lari (Detik)', validators=[DataRequired()])
    nilai_pullup = IntegerField('Nilai Pull-Up', validators=[DataRequired()])
    nilai_situp = IntegerField('Nilai Sit-Up', validators=[DataRequired()])
    nilai_pushup = IntegerField('Nilai Push-Up', validators=[DataRequired()])
    nilai_shutrun = FloatField('Nilai Shuttle Run (Detik)', validators=[DataRequired()])
    nilai_renang = FloatField('Nilai Renang (Detik)', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SocMedForm(FlaskForm):
    wa = TextAreaField('Nomor WA (628****)', validators=[Optional()])
    instagram = TextAreaField('Username instagram (bimbelikabahamas)', validators=[Optional()])
    tiktok = TextAreaField('Username tiktok (bimbelikabhamas)', validators=[Optional()])
    submit = SubmitField('Submit')