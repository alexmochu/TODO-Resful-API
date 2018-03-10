""" Imports """
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissescret'

@app.route('/')
def hello_todo():
    """Home Route"""
    response = jsonify({"Welcome message":"Welcome to TODO RestfulAPI"})
    return response

if __name__ == '__main__':
    app.run(debug=True)