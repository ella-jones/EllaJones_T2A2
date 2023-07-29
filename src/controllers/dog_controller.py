from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema
from flask_jwt_extended import jwt_required
from marshmallow import INCLUDE
from decorators.authorisation import authorise_as_employee
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes


dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')

@dogs_bp.route('/') # Method = GET
def get_all_dogs():
    # No body data input expected from user
    stmt = db.select(Dog)
    dogs = db.session.scalars(stmt)
    return dogs_schema.dump(dogs)

# The above route gets all dogs and displays them as a list.
# expected data returned = all dog records

@dogs_bp.route('/<int:id>') # Method = GET
def get_one_dog(id):
    # No body data input expected from user
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        return dog_schema.dump(dog)
    else: return {'error': f'Dog not found with id {id}'}, 404

# The above route gets the dog with the id listed in the route
# expected data return = dog record for dog with id listed in route (/<int:id>)
# If no dog exists with that id, an error message "Dog not found with id {id}" will be printed.

@dogs_bp.route('/', methods=['POST']) # Method = POST
@jwt_required() # this requires a user to be logged in in order to create (post) dogs
@authorise_as_employee # this requires users to be an employee in order to create (post) dogs
def create_dog():
    try:
        # expected input:
        # {
        #   "name": "Dog Name",
        #   "age": "4",
        #   "breed_id": 1,
        #   "gender": "Female",
        #   "description": "Dog Description"
        # }
        body_data = dog_schema.load(request.get_json(), unknown=INCLUDE) # Checks for body data inputted by user (schema.load allows for validation to occur)
        dog = Dog(
            name=body_data.get('name'),
            age=body_data.get('age'),
            breed_id=body_data.get('breed_id'),
            gender=body_data.get('gender'),
            description=body_data.get('description')
        )
        db.session.add(dog) # Adds the dog to the session
        db.session.commit() # Commit to add the dog to the database
        return dog_schema.dump(dog), 201 # Respond to the client
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column_name} is required'}, 409
        
# The above route creates a new Dog model instance
# expected data return = the new dog record that was just created + will return the breed info nested in the dog record
# If a breed_id that does not exist is used, a specific validation error will be thrown.
# If the user forgets to input a name or breed_id, a Not Null Violation will be thrown.
# If a user enters anything other than "Female", "Male", or "Other" for "gender", an error will be thrown.


@dogs_bp.route('/<int:id>', methods=['DELETE']) # Method = DELETE
@jwt_required() # user must be logged in in order to delete dogs
@authorise_as_employee # user must be an employee in order to delete dogs
def delete_one_dog(id):
    # No body data input expected from user
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog: # if the dog exists:
        db.session.delete(dog) # Deletes the dog from the session
        db.session.commit() # Commit to delete the dog from the database
        return {'message': f'Dog: {dog.name} deleted successfully'} # Respond to the client
    else:
        return {'error': f'Dog not found with id {id}'}, 404
    
# The above route will delete the dog with the id in the route
# expected data return = "Dog: {dog.name} deleted successfully"
# If the adoption does not exist, the returned data will be "Dog not found with id {id}"

@dogs_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
# Method used is 'PATCH', however, if the user tries 'PUT', it will return the same function.
@jwt_required() # user must be logged in in order to delete dogs
@authorise_as_employee # user must be an employee in order to delete dogs
def update_one_dog(id):
    # expected input: (any of the following)
    # {
    #   "name": "Dog Name",
    #   "age": "4",
    #   "breed_id": 1,
    #   "gender": "Female",
    #   "description": "Dog Description"
    # }
    body_data = dog_schema.load(request.get_json(), unknown=INCLUDE, partial=True) # Check for body data inputted by user (schema.load allows for validation)
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        dog.name = body_data.get('name') or dog.name
        dog.age = body_data.get('age') or dog.age
        dog.breed_id = body_data.get('breed_id') or dog.breed_id
        dog.gender = body_data.get('gender') or dog.gender
        dog.description = body_data.get('description') or dog.description
        db.session.commit() # Commit to add the changes for the dog to the database
        return dog_schema.dump(dog) # Respond to the client
    else:
        return {'error': f'Dog not found with id {id}'}, 404
    
# The above route will update the dog with the id listed in the route
# expected data return = the dog record that was just updated, with the updated data + will return the breed info nested in the dog record
# If a breed_id that does not exist is used, a specific validation error will be thrown.
# If the dog does not exist, the returned data will be "Dog not found with id {id}"