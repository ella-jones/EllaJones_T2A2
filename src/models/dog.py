from init import db, ma
from marshmallow import fields

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'), nullable = False)
    gender = db.Column(db.String)
    description = db.Column(db.Text)
    # adoption_id =db.Column(db.Integer, db.ForeignKey('adoptions.id'), nullable = True)

    breed = db.relationship('Breed', back_populates='dogs')
    adoption = db.relationship('Adoption', back_populates='dog')

class DogSchema(ma.Schema):
    breed = fields.Nested('BreedSchema', only=['breed_name'])
    adoption = fields.Nested('AdoptionSchema', exclude=['dog'])

    class Meta:
        fields = ('id', 'name', 'age', 'breed', 'gender', 'description', 'adoption')
        ordered = True

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)