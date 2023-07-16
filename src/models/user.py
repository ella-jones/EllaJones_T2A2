from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_employee = db.Column(db.Boolean, default=False)

    adoptions = db.relationship('Adoption', back_populates='adopter')

class UserSchema(ma.Schema):
    adoptions = fields.List(fields.Nested('AdoptionSchema', exclude=['user']))
    class Meta:
        fields = ('id', 'full_name', 'email', 'password', 'is_employee', 'adoptions')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])