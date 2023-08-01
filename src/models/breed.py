from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Breed(db.Model):
    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    breed_name = db.Column(db.String(100), nullable=False)

    dogs = db.relationship ('Dog', back_populates='breed', cascade='all, delete')

class BreedSchema(ma.Schema):
    dogs = fields.List(fields.Nested('DogSchema', exclude=['breed']))

    breed_name = fields.String(required=True, validate=And(
        Length(min=2, error='Name must be at least 2 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, spaces and numbers are allowed')
    ))

    class Meta:
        fields = ('id', 'breed_name', 'dogs')
        ordered = True

breed_schema = BreedSchema()
breeds_schema = BreedSchema(many=True)