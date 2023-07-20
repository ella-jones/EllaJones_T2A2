from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_GENDERS = ('Female', 'Male', 'Other')

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'), nullable = False)
    gender = db.Column(db.String)
    description = db.Column(db.Text)

    breed = db.relationship('Breed', back_populates='dogs')
    adoption = db.relationship('Adoption', back_populates='dog', uselist=False)

class DogSchema(ma.Schema):
    breed = fields.Nested('BreedSchema', only=['breed_name'])
    adoption = fields.Nested('AdoptionSchema', exclude=['dog'])

    gender = fields.String(validate=OneOf(VALID_GENDERS))

    class Meta:
        fields = ('id', 'name', 'age', 'breed', 'gender', 'description', 'adoption')
        ordered = True

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)