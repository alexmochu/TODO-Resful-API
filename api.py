"""Public Python Library"""
import uuid

""" Flask Extenstion Imports """
from flask import Flask, jsonify, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissescret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/chumo/Desktop/SQLite_Database/todo.db'
app.['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@app.route('/')
def hello_todo():
    """Home Route"""
    response = jsonify({"Welcome message":"Welcome to TODO RestfulAPI"})
    return response

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

if __name__ == '__main__':
    app.run(debug=True)