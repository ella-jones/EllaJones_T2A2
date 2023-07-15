from flask import Blueprint, request
from init import db
from models.breed import Breed, breeds_schema, breed_schema

breeds_bp = Blueprint('breeds', __name__, url_prefix='/breeds')

@breeds_bp.route('/')
def get_all_breeds():
    stmt = db.select(Breed)
    breeds = db.session.scalars(stmt)
    return breeds_schema.dump(breeds)
    