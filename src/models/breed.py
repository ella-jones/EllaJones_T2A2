from init import db, ma

class Breed(db.Model):
    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    breed_name = db.Column(db.String(100))

class BreedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'breed_name')
        # ordered = True (not working)

breed_schema = BreedSchema()
breeds_schema = BreedSchema(many=True)