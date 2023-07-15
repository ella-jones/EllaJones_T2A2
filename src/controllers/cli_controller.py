from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.breed import Breed

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables Created')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables Dropped')

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            full_name='Jane Doe',
            email='employee1@email.com',
            password=bcrypt.generate_password_hash('employee1pw').decode('utf-8'),
            is_employee=True
        ),
        User(
            full_name='John Smith',
            email='user1@email.com',
            password=bcrypt.generate_password_hash('user1pw').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    breeds = [
        Breed(
            breed_name='Labrador',
        ),
        Breed(
            breed_name='Boston Terrier'
        ),
        Breed(
            breed_name='Golden Retriever'
        ),
        Breed(
            breed_name='German Shepard'
        ),
        Breed(
            breed_name='Pug'
        )
    ]

    db.session.add_all(breeds)

    db.session.commit()

    print("Tables Seeded")