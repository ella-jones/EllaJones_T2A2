from flask import Blueprint, request
from init import db
from models.breed import Breed, breeds_schema, breed_schema
from flask_jwt_extended import jwt_required
from controllers.dog_controller import authorise_as_employee
from sqlalchemy.exc import IntegrityError

breeds_bp = Blueprint('breeds', __name__, url_prefix='/breeds')

@breeds_bp.route('/')
def get_all_breeds():
    stmt = db.select(Breed)
    breeds = db.session.scalars(stmt)
    return breeds_schema.dump(breeds)
    
@breeds_bp.route('/<int:id>')
def get_one_breed(id):
    stmt = db.select(Breed).filter_by(id=id)
    breed = db.session.scalar(stmt)
    if breed:
        return breed_schema.dump(breed)
    else: return {'error': f'Breed not found with id {id}'}, 404

@breeds_bp.route('/', methods=['POST'])
@jwt_required()
@authorise_as_employee
def create_breed():
    body_data = breed_schema.load(request.get_json())
    # creates a new Breed model instance
    breed = Breed(
        breed_name=body_data.get('breed_name'),   
    )
    db.session.add(breed)
    db.session.commit()
    return breed_schema.dump(breed), 201

@breeds_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_employee
def delete_one_breed(id):
    try:
        stmt = db.select(Breed).filter_by(id=id)
        breed = db.session.scalar(stmt)
        if breed:
            db.session.delete(breed)
            db.session.commit()
            return {'message': f'Breed: {breed.breed_name} deleted successfully'}
        else:
            return {'error': f'Breed not found with id {id}'}, 404
    except IntegrityError as err:
        return {'error': f'Cannot delete breed with id {id} as it has dogs associated.'}

@breeds_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
@authorise_as_employee
def update_one_breed(id):
    body_data = breed_schema.load(request.get_json(), partial=True)
    stmt = db.select(Breed).filter_by(id=id)
    breed = db.session.scalar(stmt)
    if breed:
        breed.breed_name = body_data.get('breed_name') or breed.breed_name
        db.session.commit()
        return breed_schema.dump(breed)
    else:
        return {'error': f'Breed not found with id {id}'}, 404

