from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import INCLUDE
import functools

dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')

def authorise_as_employee(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(stmt)
        if user.is_employee:
            return fn(*args, **kwargs)
        else: 
            return {'error': 'Not authorised to perform action'}, 403
    return wrapper

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
@jwt_required()
@authorise_as_employee
def create_dog():
    body_data = dog_schema.load(request.get_json(), unknown=INCLUDE)
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
@authorise_as_employee
def delete_one_dog(id):
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        db.session.delete(dog)
        db.session.commit()
        return {'message': f'Dog: {dog.name} deleted successfully'}
    else:
        return {'error': f'Dog not found with id {id}'}, 404

@dogs_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
@authorise_as_employee
def update_one_dog(id):
    body_data = dog_schema.load(request.get_json(), unknown=INCLUDE, partial=True)
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        dog.name = body_data.get('name') or dog.name
        dog.age = body_data.get('age') or dog.age
        dog.breed_id = body_data.get('breed_id') or dog.breed_id
        dog.gender = body_data.get('gender') or dog.gender
        dog.description = body_data.get('description') or dog.description
        db.session.commit()
        return dog_schema.dump(dog)
    else:
        return {'error': f'Dog not found with id {id}'}, 404