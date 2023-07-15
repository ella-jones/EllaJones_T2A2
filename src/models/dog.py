from init import db, ma
from marshmallow import fields

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'), nullable = False)
    
    gender = db.Column(db.String)
    description = db.Column(db.text)
    is_adopted = db.Column(db.Boolean, default=False)

    breed = db.relationship('Breed', back_populates='dogs')

class DogSchema(ma.Schema):
    breed = fields.Nested('BreedSchema', only=['breed_name'])

    class Meta:
        fields = ('id', 'name', 'age', 'breed', 'gender', 'description', 'is_adopted')
        ordered = True

dog_schema = DogSchema()
dog_schema = DogSchema(many=True)