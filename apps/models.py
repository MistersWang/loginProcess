from app import db
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @validates('username')
    def validate_username(self, key, username):
        if not username.isalnum():
            raise ValueError("Username must have only letters and numbers")
        return username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)