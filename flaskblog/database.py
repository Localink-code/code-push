# Import database instance from main application
from flaskblog import db

# User model for storing user account information
class User(db.Model):
    # Primary key - auto-incrementing user ID
    id=db.Column(db.Integer,primary_key=True)
    
    # Username field - unique, required, max 20 characters
    username=db.Column(db.String(20),unique=True,nullable=False)
    
    # Email field - unique, required, max 120 characters
    email=db.Column(db.String(120),unique=True,nullable=False)
    
    # Password field - required, max 60 characters (for hashed passwords)
    password=db.Column(db.String(60),nullable=False)


class Admin(db.Model):
    # Primary key - auto-incrementing admin ID
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    # Username field - unique, required, max 20 characters
    # Email field - unique, required, max 120 characters
    # Password field - required, max 60 characters (for hashed passwords)



