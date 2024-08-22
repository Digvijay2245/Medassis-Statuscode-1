from app import db, session
from app import bcrypt
from flask_login import UserMixin
from datetime import datetime

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(length=30), nullable=False, unique=True)
    email_address=db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash=db.Column(db.String(length=60), nullable=False)
    checkups=db.relationship('Checkup', backref='patient_checked', lazy=True)
    gender=db.Column(db.String(length=50), nullable=True)
    age=db.Column(db.Integer(), nullable=True)
    height=db.Column(db.Float(), nullable=True)
    weight=db.Column(db.Float(), nullable=True)
    pincode=db.Column(db.Integer(), nullable=True)
    phone=db.Column(db.Integer(), nullable=True)
    city=db.Column(db.String(length=50), nullable=True)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Doctor(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(length=30), nullable=False, unique=True)
    email_address=db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash=db.Column(db.String(length=60), nullable=False)
    specialization=db.Column(db.String(length=100))
    pincode=db.Column(db.Integer())
    gender=db.Column(db.String(length=50), nullable=True)
    age=db.Column(db.Integer())
    availability=db.Column(db.String(), default=True)
    phone=db.Column(db.Integer(), nullable=True)
    city=db.Column(db.String(length=50), nullable=True)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    

class Checkup(db.Model):
    form_id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(), nullable=False)
    age=db.Column(db.Integer(), nullable=False)
    gender=db.Column(db.String(), nullable=False)
    smoking_history=db.Column(db.String(), nullable=False)
    hypertension=db.Column(db.Integer(), nullable=False)
    heart_disease=db.Column(db.Integer(), nullable=False)
    blood_glucose=db.Column(db.Float(), nullable=False)
    weight=db.Column(db.Float(), nullable=False)
    height=db.Column(db.Float(), nullable=False)
    hba1c=db.Column(db.String(), nullable=False)
    diabetes=db.Column(db.Integer(), nullable=False)
    patient_id=db.Column(db.Integer(), db.ForeignKey('user.id'))

class Kidney(db.Model):
    form_id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(), nullable=False)
    age=db.Column(db.Integer(), nullable=False)
    gender=db.Column(db.String(), nullable=False)
    height=db.Column(db.Float(), nullable=False)
    weight=db.Column(db.Float(), nullable=False)
    smok_alc=db.Column(db.String(), nullable=False)
    physical_act=db.Column(db.Integer(), nullable=False)
    kidney_diet=db.Column(db.Integer(), nullable=False)
    fhkd=db.Column(db.String(), nullable=False)
    fhh=db.Column(db.String(), nullable=False)
    fhd=db.Column(db.String(), nullable=False)
    urinary=db.Column(db.String(), nullable=False)
    systolic_bp=db.Column(db.Integer(), nullable=False)
    diastolic_bp=db.Column(db.Integer(), nullable=False)
    blood_sugar=db.Column(db.Integer(), nullable=False)
    hba1c=db.Column(db.Float(), nullable=False)
    serum=db.Column(db.Float(), nullable=False)
    bun_lvl=db.Column(db.Float(), nullable=False)
    gfr=db.Column(db.Float(), nullable=False)
    protein_urine=db.Column(db.Float(), nullable=False)
    sodium_electrolyte=db.Column(db.Float(), nullable=False)
    potassium_electrolyte=db.Column(db.Float(), nullable=False)
    hemoglobin=db.Column(db.Float(), nullable=False)
    cholesterol=db.Column(db.Float(), nullable=False)
    diuretics=db.Column(db.String(), nullable=False)
    edema=db.Column(db.String(), nullable=False)
    muscle_cramps=db.Column(db.String(), nullable=False)
    itching=db.Column(db.String(), nullable=False)
    kidney_per=db.Column(db.Float(), nullable=False)
    patient_id=db.Column(db.Integer(), db.ForeignKey('user.id'))

class Liver(db.Model):
    form_id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(), nullable=False)
    age=db.Column(db.Integer(), nullable=False)
    gender=db.Column(db.String(), nullable=False)
    total_protein=db.Column(db.Float(), nullable=False)
    albumin=db.Column(db.Float(), nullable=False)
    ag_ratio=db.Column(db.Float(), nullable=False)
    total_bilirubin=db.Column(db.Float(), nullable=False)
    direct_bilirubin=db.Column(db.Float(), nullable=False)
    alkaline_phosphate=db.Column(db.Integer(), nullable=False)
    sgpt=db.Column(db.Integer(), nullable=False)
    sgot=db.Column(db.Integer(), nullable=False)
    height=db.Column(db.Float(), nullable=False)
    weight=db.Column(db.Float(), nullable=False)
    liver_per=db.Column(db.Float(), nullable=False)
    patient_id=db.Column(db.Integer(), db.ForeignKey('user.id'))
    
class Reminder(db.Model):
    reminder_id=db.Column(db.Integer(), primary_key=True)
    #name=db.Column(db.String(), nullable=False)
    email_address=db.Column(db.String(length=50), nullable=False)
    medicine=db.Column(db.String(length=50), nullable=False)
    reminder_time=db.Column(db.DateTime(), nullable=False)
    sent=db.Column(db.Boolean(), default=False)
    

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.relationship('User', backref=db.backref('messages', lazy=True))
