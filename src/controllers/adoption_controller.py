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
    # No body data input expected from user
    stmt = db.select(Adoption)
    adoptions = db.session.scalars(stmt)
    return adoptions_schema.dump(adoptions)

# The above route gets all adoptions and displays them as a list.
# expected data returned = all adoption records


@adoptions_bp.route('/<int:id>') # Method = GET
def get_one_adoption(id):
    # No body data input expected from user
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        return adoption_schema.dump(adoption)
    else: return {'error': f'Adoption not found with id {id}'}, 404

# The above route gets the adoption with the id listed in the route
# expected data return = adoption record for adoption with id listed in route (/<int:id>)
# If no adoption exists with that id, an error message "Adoption not found with id {id}" will be printed.

@adoptions_bp.route('/', methods=['POST']) # Method = POST
@jwt_required() # this requires a user to be logged in in order to create (post) adoptions
@authorise_as_employee # this requires users to be an employee in order to create (post) adoptions
def create_adoption():
    try:
        # expected input:
        # {
        #   "dog_id": 1,
        #   "adopter_id": 1,
        #   "notes": "Adoption 1 Notes"
        # }
        body_data = adoption_schema.load(request.get_json(), unknown=INCLUDE) # Checks for body data inputted by user (schema.load allows for validation to occur)
        adoption = Adoption(
            dog_id=body_data.get('dog_id'),
            adopter_id=body_data.get('adopter_id'),
            # No date needs to be entered by the user as it will automatically 
            # set to the current date when a new adoption is created
            adoption_date=body_data.get('adoption_date'),
            notes=body_data.get('notes') 
        )
        db.session.add(adoption) # Adds the adoption to the session
        db.session.commit() # Commit to add the adoption to the database
        return adoption_schema.dump(adoption), 201 # Respond to the client
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column_name} is required'}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'An adoption record for that dog already exists'}, 409

# The above route creates a new Adoption model instance
# expected data return = the new adoption record that was just created + will return the dog and adopter info nested in the adoption record
# If a dog_id or adopter_id that does not exist is used, a specific validation error will be thrown.
# If a user attemps to create an adoption for a dog that has already been adopted, a Unique violation error will be thrown.
# If the user forgets to input either a dog_id or adopter_id, a Not Null Violation will be thrown.

@adoptions_bp.route('/<int:id>', methods=['DELETE']) # Method = DELETE
@jwt_required() # user must be logged in in order to delete adoptions
@authorise_as_employee # user must be an employee in order to delete adoptions
def delete_one_adoption(id):
    # No body data input expected from user
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption: # if the adoption exists:
        db.session.delete(adoption) # Deletes the adoption from the session
        db.session.commit() # Commit to delete the adoption from the database
        return {'message': f'Adoption with {id} was deleted successfully'} # Respond to the client
    else:
        return {'error': f'Adoption not found with id {id}'}, 404
    
# The above route will delete the adoption with the id in the route
# expected data return = "Adoption with {id} was deleted successfully"
# If the adoption does not exist, the returned data will be "Adoption not found with id {id}"
    
@adoptions_bp.route('/<int:id>', methods=['PUT', 'PATCH']) 
# Method used is 'PATCH', however, if the user tries 'PUT', it will return the same function.
@jwt_required() # user must be logged in in order to delete adoptions
@authorise_as_employee # user must be an employee in order to delete adoptions
def update_one_adoption(id):
    # expected input: (any of the following)
    # {
    #   "dog_id": 1,
    #   "adopter_id": 1,
    #   "notes": "Adoption 1 Notes"
    # }
    body_data = adoption_schema.load(request.get_json(), unknown=INCLUDE, partial=True) # Check for body data inputted by user (schema.load allows for validation)
    stmt = db.select(Adoption).filter_by(id=id)
    adoption = db.session.scalar(stmt)
    if adoption:
        adoption.dog_id = body_data.get('dog_id') or adoption.dog_id
        adoption.adopter_id = body_data.get('adopter_id') or adoption.adopter_id
        adoption.adoption_date = body_data.get('adoption_date') or adoption.adoption_date
        adoption.notes = body_data.get('notes') or adoption.notes
        db.session.commit() # Commit to add the changes for the adoption to the database
        return adoption_schema.dump(adoption) # Respond to the client
    else:
        return {'error': f'Adoption not found with id {id}'}, 404

# The above route will update the adoption with the id listed in the route
# expected data return = the adoption record that was just updated, with the updated data + will return the dog and adopter info nested in the adoption record
# If a dog_id or adopter_id that does not exist is used, a specific validation error will be thrown.
# If the adoption does not exist, the returned data will be "Adoption not found with id {id}"