from flask import request, redirect, jsonify

from app import app, db

@app.route('/', methods=['GET'])
def hello_world():
    return "hello world"