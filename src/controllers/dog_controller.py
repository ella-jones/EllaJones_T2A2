from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema
# from controllers.cli_controller import breeds

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

# @dogs_bp.route('/', methods=['POST'])
# def create_dog():
#     body_data = request.get_json()
#     # create a new Dog model instance
#     dog = Dog(
#         name=body_data.get('name'),
#         age=body_data.get('age'),
#         breed=breeds[body_data.get('breed')],
#         gender=body_data.get('gender'),
#         description=body_data.get('description')    
#     )

#     db.session.add(dog)
#     db.session.commit()
#     return dog_schema.dump(dog), 201

