from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema
from flask_jwt_extended import jwt_required

dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')

@dogs_bp.route('/')
def get_all_dogs():
    stmt = db.select(Dog)
    dogs = db.session.scalars(stmt)
    return dogs_schema.dump(dogs)

@dogs_bp.route('/<int:id>')
def get_one_dog(id):
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        return dog_schema.dump(dog)
    else: return {'error': f'Dog not found with id {id}'}, 404

@dogs_bp.route('/', methods=['POST'])
def create_dog():
    body_data = request.get_json()
    # create a new Dog model instance
    dog = Dog(
        name=body_data.get('name'),
        age=body_data.get('age'),
        breed_id=body_data.get('breed_id'),
        gender=body_data.get('gender'),
        description=body_data.get('description')    
    )
    db.session.add(dog)
    db.session.commit()
    return dog_schema.dump(dog), 201

@dogs_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_dog(id):
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        db.session.delete(dog)
        db.session.commit()
        return {'message': f'Dog {dog.name} deleted successfully'}
    else:
        return {'error': f'Dog not found with id {id}'}, 404

@dogs_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_dog(id):
    body_data = request.get_json()
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        dog.name = body_data.get('name') or dog.name
        dog.age = body_data.get('age') or dog.age
        dog.breed_id = body_data.get('breed_id') or dog.breed_id
        dog.gender = body_data.get('gender') or dog.gender
        dog.description = body_data.get('description') or dog.description
        dog.is_adopted = body_data.get('is_adopted') or dog.is_adopted
        db.session.commit()
        return dog_schema.dump(dog)
    else:
        return {'error': f'Dog not found with id {id}'}, 404

