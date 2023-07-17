from init import db, ma
from marshmallow import fields
from datetime import date

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

    class Meta:
        fields = ('id', 'dog', 'adopter', 'adoption_date', 'notes')
        ordered = True

adoption_schema = AdoptionSchema()
adoptions_schema = AdoptionSchema(many=True)