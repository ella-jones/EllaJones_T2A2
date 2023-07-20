from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import OneOf
from marshmallow.exceptions import ValidationError

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

    @validates('breed_id')
    def validate_breed_id(self, value):
            stmt = db.select(db.func.count()).select_from(Dog).filter_by(breed_id=value)
            count=db.session.scalar(stmt)
            if count < 1 :
                raise ValidationError(f'No breed with that id exists')

    class Meta:
        fields = ('id', 'name', 'age', 'breed', 'gender', 'description', 'adoption', 'breed_id')
        ordered = True
        include_fk = True

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)