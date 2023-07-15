from init import db, ma

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.Strong, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_employee = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'email', 'password', 'is_employee')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])