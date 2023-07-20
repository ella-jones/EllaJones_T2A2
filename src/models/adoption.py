from init import db, ma
from marshmallow import fields, validates
from datetime import date
from marshmallow.exceptions import ValidationError

class Adoption(db.Model):
    __tablename__ = 'adoptions'

    id = db.Column(db.Integer, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.id'), nullable=False)
    adopter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    adoption_date = db.Column(db.Date, default=date.today()) # date created
    notes = db.Column(db.Text)

    adopter = db.relationship('User', back_populates='adoptions')
    dog = db.relationship('Dog', back_populates='adoption')
    
class AdoptionSchema(ma.Schema):
    adopter = fields.Nested('UserSchema', only=['full_name', 'email'])
    dog = fields.Nested('DogSchema', only=['name'])

    @validates('dog_id')
    def validate_dog_id(self, value):
            stmt = db.select(db.func.count()).select_from(Adoption).filter_by(dog_id=value)
            count=db.session.scalar(stmt)
            if count > 0 :
                raise ValidationError(f'An adoption record for that dog already exists')

    class Meta:
        fields = ('id', 'dog', 'adopter', 'adoption_date', 'notes', 'dog_id')
        ordered = True
        include_fk = True

adoption_schema = AdoptionSchema()
adoptions_schema = AdoptionSchema(many=True)