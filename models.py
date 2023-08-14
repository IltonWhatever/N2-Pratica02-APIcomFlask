# Modelo
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='Tutor', lazy=True, cascade="all, delete") # D

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "pets": self.pets}



class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id', ondelete="CASCADE"), nullable=False) # D

    def serialize(self):
        return {"id": self.id,
                "nome": self.nome,
                "tutor_id": self.tutor_id}


# D
class PetSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "tutor_id")

class TutorSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "pets")
    pet = ma.Nested(PetSchema)
