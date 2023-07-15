from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema

dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')

@dogs_bp.route('/')
def get_all_dogs():
    stmt = db.select(Dog)
    dogs = db.session.scalars(stmt)
    return dogs_schema.dump(dogs)