from flask import Blueprint, request
from init import db
from models.adoption import Adoption, adoptions_schema, adoption_schema
from flask_jwt_extended import jwt_required
from marshmallow import INCLUDE
from decorators.authorisation import authorise_as_employee

adoptions_bp = Blueprint('adoptions', __name__, url_prefix='/adoptions')

@adoptions_bp.route('/')
def get_all_adoptions():
    stmt = db.select(Adoption)
    adoptions = db.session.scalars(stmt)
    return adoptions_schema.dump(adoptions)

@adoptions_bp.route('/<int:id>')
def get_one_adoption(id):
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        return adoption_schema.dump(adoption)
    else: return {'error': f'Adoption not found with id {id}'}, 404

@adoptions_bp.route('/', methods=['POST'])
@jwt_required()
@authorise_as_employee
def create_adoption():
    body_data = adoption_schema.load(request.get_json(), unknown=INCLUDE)
    # create a new Adoption model instance
    adoption = Adoption(
        dog_id=body_data.get('dog_id'),
        adopter_id=body_data.get('adopter_id'),
        adoption_date=body_data.get('adoption_date'),
        notes=body_data.get('notes') 
    )
    db.session.add(adoption)
    db.session.commit()
    return adoption_schema.dump(adoption), 201

@adoptions_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_employee
def delete_one_adoption(id):
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        db.session.delete(adoption)
        db.session.commit()
        return {'message': f'Adoption with {id} was deleted successfully'}
    else:
        return {'error': f'Adoption not found with id {id}'}, 404
    
@adoptions_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
@authorise_as_employee
def update_one_adoption(id):
    body_data = adoption_schema.load(request.get_json(), unknown=INCLUDE, partial=True)
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        adoption.dog_id = body_data.get('dog_id') or adoption.dog_id
        adoption.adopter_id = body_data.get('adopter_id') or adoption.adopter_id
        adoption.adoption_date = body_data.get('adoption_date') or adoption.adoption_date
        adoption.notes = body_data.get('notes') or adoption.notes
        db.session.commit()
        return adoption_schema.dump(adoption)
    else:
        return {'error': f'Adoption not found with id {id}'}, 404