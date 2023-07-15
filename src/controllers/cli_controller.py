from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.breed import Breed
from models.dog import Dog

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

    dogs = [
        Dog (
            name='Dog 1',
            age='3 and a half',
            breed=breeds[0],
            gender='Female',
            description='Dog 1 desc'
        ),
        Dog (
            name='Dog 2',
            age='5',
            breed=breeds[1],
            gender='Male',
            description='Dog 2 desc',
            is_adopted=True
        ),
        Dog (
            name='Dog 3',
            age='1',
            breed=breeds[0],
            gender='Male',
            description='Dog 3 desc'
        ),
        Dog (
            name='Dog 4',
            age='4',
            breed=breeds[2],
            gender='Female',
            description='Dog 4 desc'
        )
    ]

    db.session.add_all(dogs)
    db.session.commit()

    print("Tables Seeded")