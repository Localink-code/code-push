# Import necessary Flask modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Create Flask application instance
app=Flask(__name__)

# Configure secret key for session management and CSRF protection
app.config["SECRET_KEY"]='Hg_-23M840HRczgGNv2Lz-u0lMIer4WBgbwJfbzQMrI'

# Configure SQLite database URI
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'

# Initialize SQLAlchemy database object
db=SQLAlchemy(app)

# Push application context to enable database operations
app.app_context().push()
login_manager=LoginManager(app)
login_manager.login_view="login"



# Import routes and database models (must be after app and db initialization)
from flaskblog import route
from flaskblog.database import User