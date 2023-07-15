from init import db, ma
from marshmallow import fields

class Breed(db.Model):
    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    breed_name = db.Column(db.String(100))

    dogs = db.relationship ('Dog', back_populated='breed', cascade='all, delete')

class BreedSchema(ma.Schema):
    dogs = fields.List(fields.Nested('DogSchema', exclude=['breed']))
    class Meta:
        fields = ('id', 'breed_name', 'dogs')
        # ordered = True (not working)

breed_schema = BreedSchema()
breeds_schema = BreedSchema(many=True)