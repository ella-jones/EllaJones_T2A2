from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST']) # Method = POST
def auth_register():
    try:
        # expected input:
        # {
        #   "full_name": "Jane Doe",
        #   "email": "user@email.com",
        #   "password": "user1pw"
        # }
        body_data = request.get_json() # Checks for body data inputted by user
        user = User()
        user.full_name = body_data.get('full_name')
        user.email = body_data.get('email')
        if body_data.get('password'):
            user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') # encrypts the password so that it is not readable in the database
        db.session.add(user) # Add the user to the session
        db.session.commit() # Commit to add the user to the database
        return user_schema.dump(user), 201 # Respond to the client

    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'Email address already in use'}, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column_name} is required'}, 409
        
# The above route creates a new User model instance from the user info
# expected data return = the new user's information that was just created
# If a user attemps to create a user with an email that has already been used, a Unique Violation error will be thrown.
# If the user forgets to enter the name, email or password, a Not Null Violation error will be thrown.

@auth_bp.route('/login', methods=['POST']) # Method = POST
def auth_login():
    body_data = request.get_json() # Checks for body data inputted by user
    # expected input:
        # {
        #   "email": "user@email.com",
        #   "password": "user1pw"
        # }

    # Find the user by email address
    stmt = db.select(User).filter_by(email=body_data.get('email'))
    user = db.session.scalar(stmt)

    # If user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get('password')):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1)) # this token will expire in 1 day.
        return { 'email': user.email, 'token': token, 'is_employee': user.is_employee }
    else:
        return { 'error': 'Invalid email or password' }, 401
    
# The above route is used for a user to log in and receive their access token.
# expected data return = email, token and "is_employee" status of user that is now logged in.
# if the user enters an invalid email or password, an error will be thrown.
    
