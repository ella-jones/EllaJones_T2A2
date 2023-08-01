from flask import Blueprint, request
from init import db
from models.breed import Breed, breeds_schema, breed_schema
from flask_jwt_extended import jwt_required
from decorators.authorisation import authorise_as_employee
from sqlalchemy.exc import IntegrityError

breeds_bp = Blueprint('breeds', __name__, url_prefix='/breeds')

@breeds_bp.route('/') # Method = GET
def get_all_breeds():
    # No body data input expected from user
    stmt = db.select(Breed)
    breeds = db.session.scalars(stmt)
    return breeds_schema.dump(breeds)

# The above route gets all breeds and displays them as a list.
# expected data returned = all breeds
    
@breeds_bp.route('/<int:id>') # Method = GET
def get_one_breed(id):
    # No body data input expected from user
    stmt = db.select(Breed).filter_by(id=id)
    breed = db.session.scalar(stmt)
    if breed:
        return breed_schema.dump(breed)
    else: return {'error': f'Breed not found with id {id}'}, 404

# The above route gets the breed with the id listed in the route
# expected data return = breed information for breed with id listed in route (/<int:id>)
# If no breed exists with that id, an error will be thrown.

@breeds_bp.route('/', methods=['POST']) # Method = POST
@jwt_required() # this requires a user to be logged in in order to create (post) adoptions
@authorise_as_employee # this requires users to be an employee in order to create (post) adoptions
def create_breed():
    # expected input:
        # {
        #   "breed_name": "Pug"
        # }
    body_data = breed_schema.load(request.get_json()) # Checks for body data inputted by user (schema.load allows for validation to occur)
    # creates a new Breed model instance
    breed = Breed(
        breed_name=body_data.get('breed_name'),   
    )
    db.session.add(breed) # Adds the breed to the session
    db.session.commit() # Commit to add the breed to the database
    return breed_schema.dump(breed), 201 # Respond to the client

# The above route creates a new Breed model instance
# expected data return = the new breed that was just created
# If a user enters a breed_name with less than two letters a specific error will be thrown
# If a user enters a breed_name which includes special characters, a specific error will be thrown.

@breeds_bp.route('/<int:id>', methods=['DELETE']) # Method = DELETE
@jwt_required()# user must be logged in in order to delete breeds
@authorise_as_employee # user must be an employee in order to delete breeds
def delete_one_breed(id):
    # No body data input expected from user
    try:
        stmt = db.select(Breed).filter_by(id=id)
        breed = db.session.scalar(stmt)
        if breed:
            db.session.delete(breed) # Deletes the breed from the session
            db.session.commit() # Commit to delete the breed from the database
            return {'message': f'Breed: {breed.breed_name} deleted successfully'} # Respond to the client
        else:
            return {'error': f'Breed not found with id {id}'}, 404
    except IntegrityError as err:
        return {'error': f'Cannot delete breed with id {id} as it has dogs associated.'}

# The above route will delete the breed with the id in the route
# expected data return = "Breed: {breed.breed_name} deleted successfully"
# If the breed does not exist, the returned data will be "Breed not found with id {id}"
# If the breed has dogs linked to it, it is not deletable and an error message will be displayed to the user.

@breeds_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
# Method used is 'PATCH', however, if the user tries 'PUT', it will return the same function.
@jwt_required() # user must be logged in in order to delete breeds
@authorise_as_employee # user must be an employee in order to delete breeds
def update_one_breed(id):
    # expected input:
    # {
    #   "breed_name": "Pug Updated Name"
    # }
    body_data = breed_schema.load(request.get_json(), partial=True) # Check for body data inputted by user (schema.load allows for validation)
    stmt = db.select(Breed).filter_by(id=id)
    breed = db.session.scalar(stmt)
    if breed:
        breed.breed_name = body_data.get('breed_name') or breed.breed_name
        db.session.commit() # Commit to add the changes for the breed to the database
        return breed_schema.dump(breed) # Respond to the client
    else:
        return {'error': f'Breed not found with id {id}'}, 404

# The above route will update the breed with the id listed in the route
# expected data return = the breed that was just updated, with the updated data
# If the breed does not exist, the returned data will be "Breed not found with id {id}"