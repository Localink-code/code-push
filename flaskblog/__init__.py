from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SECRET_KEY"]='Hg_-23M840HRczgGNv2Lz-u0lMIer4WBgbwJfbzQMrI'
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'
db=SQLAlchemy(app)
app.app_context().push()
from flaskblog import route
from flaskblog.database import User