from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "this is a super secure key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://isniccsljdtumx:JlZuUgfrD6wTfCIJBGR18cHv6O@ec2-54-83-3-38.compute-1.amazonaws.com:5432/d3ensk0kcg15sa"
db = SQLAlchemy(app)
from app import views
from app.models import User