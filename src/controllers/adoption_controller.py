from flask import Blueprint, request
from init import db
from models.adoption import Adoption, adoptions_schema, adoption_schema
from flask_jwt_extended import jwt_required
from marshmallow import INCLUDE
from decorators.authorisation import authorise_as_employee
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

adoptions_bp = Blueprint('adoptions', __name__, url_prefix='/adoptions')

@adoptions_bp.route('/') # Method = GET
def get_all_adoptions():
    # Gets all adoptions and displays them as a list.
    # No body data input expected from user
    stmt = db.select(Adoption)
    adoptions = db.session.scalars(stmt)
    return adoptions_schema.dump(adoptions)

# expected data returned = all adoption records


@adoptions_bp.route('/<int:id>') # Method = Get
def get_one_adoption(id):
    # Gets adoption with a specific id
    # No body data input expected from user
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        return adoption_schema.dump(adoption)
    else: return {'error': f'Adoption not found with id {id}'}, 404

# expected data return = adoption record for adoption with id listed in route (/<int:id>)

@adoptions_bp.route('/', methods=['POST']) # Method = Post
@jwt_required()
# user must be an employee in order to create (post) adoptions
@authorise_as_employee
def create_adoption():
    try:
        # Check for body data inputted by user (schema.load allows for validation)
        # expected input:
        # {
        #   "dog_id" = 1
        #   "adopter_id" = 1
        #   "notes" = "Adoption 1 Notes"
        # }
        body_data = adoption_schema.load(request.get_json(), unknown=INCLUDE)
        # create a new Adoption model instance
        adoption = Adoption(
            dog_id=body_data.get('dog_id'),
            adopter_id=body_data.get('adopter_id'),
            # No date needs to be entered by the user as it will automatically 
            # set to the current date when a new adoption is created
            adoption_date=body_data.get('adoption_date'),
            notes=body_data.get('notes') 
        )
        db.session.add(adoption)
        db.session.commit()
        return adoption_schema.dump(adoption), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column_name} is required'}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'An adoption record for that dog already exists'}, 409

# expected data return = the new adoption record that was just created
# will return the dog and adopter info nested in the adoption record
# If a dog_id or adopter_id that does not exist is used, a specific validation error will be thrown.
# If a user attemps to create an adoption for a dog that has already been adopted, a Unique violation error will be thrown.
# If the user forgets to input either a dog_id or adopter_id, a Not Null Violation will be thrown.

@adoptions_bp.route('/<int:id>', methods=['DELETE']) # Method = Delete
@jwt_required()
# user must be an employee in order to delete adoptions
@authorise_as_employee
def delete_one_adoption(id):
    # Delete adoption with a specific id
    # No body data input expected from user
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        db.session.delete(adoption)
        db.session.commit()
        return {'message': f'Adoption with {id} was deleted successfully'}
    else:
        return {'error': f'Adoption not found with id {id}'}, 404
    
# expected data return = "Adoption with {id} was deleted successfully"
# If the adoption does not exist, the returned data will be "Adoption not found with id {id}"

    
@adoptions_bp.route('/<int:id>', methods=['PUT', 'PATCH']) 
# Method used is 'PATCH', however, if the user tries 'PUT', it will return the same function.
@jwt_required()
@authorise_as_employee
def update_one_adoption(id):
    # Check for body data inputted by user (schema.load allows for validation)
    # expected input:
    # {
    #   "dog_id" = 1
    #   "adopter_id" = 1
    #   "notes" = "Adoption 1 Notes"
    # }
    body_data = adoption_schema.load(request.get_json(), unknown=INCLUDE, partial=True)
    # Update adoption with a specific id
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
    
# expected data return = the adoption record that was just updated
# will return the dog and adopter info nested in the adoption record
# If a dog_id or adopter_id that does not exist is used, a specific validation error will be thrown.
# # If the adoption does not exist, the returned data will be "Adoption not found with id {id}"