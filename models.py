# Modelo
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='Tutor', lazy=True, cascade="all, delete") # D

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id', ondelete="CASCADE"), nullable=False) # D

# D
class PetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet

    id = ma.auto_field()
    nome = ma.auto_field()
    tutor_id = ma.auto_field()

class TutorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tutor
    
    id = ma.auto_field()
    nome = ma.auto_field()
    pets = ma.auto_field()
