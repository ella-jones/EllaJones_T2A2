from init import db
from models.user import User
from flask_jwt_extended import get_jwt_identity
import functools

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