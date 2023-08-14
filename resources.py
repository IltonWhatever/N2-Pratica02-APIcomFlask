# Resources
from flask_restful import Resource, reqparse, abort
from flask import jsonify
from models import db,Tutor,Pet,TutorSchema,PetSchema

class TutorResource(Resource):
    def get(self, tutor_id=None):
        if tutor_id is None:
            tutor = Tutor.query.all()
            return TutorSchema(many=True).dumps(tutor),200
        
        tutor = Tutor.query.get(tutor_id)
        #return TutorSchema().jsonify(tutor)
        #return TutorSchema().dump(tutor), 200
        tutorschema = TutorSchema()
        result = tutorschema.dump(tutor)
        return jsonify(result)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args = parser.parse_args()
        tutor = Tutor(nome=args['nome_tutor'])
        db.session.add(tutor)
        db.session.commit()
        return TutorSchema().dump(tutor), 201
    
    def delete(self, tutor_id=None):
        if tutor_id is None:
            abort(404, message="ID {} do tutor não encontrado".format(tutor_id))
        Tutor.query.filter_by(id=tutor_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Tutor {} Deletado com Sucesso".format(tutor_id)
        })
    
    def put(self, tutor_id=None):
        if tutor_id is None:
            abort(404, message="ID {} do tutor não encontrado".format(tutor_id))
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args = parser.parse_args()
        tutor = Tutor.query.get(tutor_id)
        tutor.nome = args["nome_tutor"]
        db.session.commit()
        return TutorSchema().dump(tutor), 201
    
class PetResource(Resource):
    def get(self, pet_id=None):
        if pet_id:
            pet = Pet.query.all()
            return PetSchema(many=True).dumps(pet),200

        pet = Pet.query.get(pet_id)
        #return jsonify(PetSchema().dump(pet))
        return PetSchema().dump(pet), 200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_pet', type=str, required=True)
        parser.add_argument('tutor_id', type=int, required=True)
        args = parser.parse_args()

        pet = Pet(nome=args['nome_pet'], tutor_id=args['tutor_id'])
        db.session.add(pet)
        db.session.commit()
        return TutorSchema().dump(pet), 201
    
    def put(self, pet_id=None):
        if pet_id is None:
            abort(404, message="ID pet não encontrado")
        
        parser = reqparse.RequestParser()
        parser.add_argument('nome_pet', type=str, required=True)
        parser.add_argument('tutor_id', type=int, required=True)
        args = parser.parse_args()

        pet = Pet.query.get(pet_id)

        pet.nome = args["nome_pet"]
        pet.tutor_id = args["tutor_id"]

        db.session.commit()
        return TutorSchema().dump(pet), 201
    
    def delete(self, pet_id=None):
        if pet_id is None:
             abort(404, message="ID {} do pet não encontrado".format(pet_id))
        Pet.query.filter_by(id=pet_id).delete()
        db.session.commit()

        return jsonify(msg = {
            "Resposta": "Pet {} Deletado com Sucesso".format(pet_id)
        })
    
        