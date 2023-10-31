from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = 'Hello Backend'
    return jsonify(data)