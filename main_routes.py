from flask import Blueprint, jsonify, request
import pymongo
from pymongo import MongoClient
import certifi

ca_file = certifi.where()
cluster = MongoClient("mongodb+srv://farhanmnavas:1234farhan5678@cluster0.vmoxzj4.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca_file)

db = cluster["rhdevs"]
collection = db["farhan"]

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = 'Hello Backend'
    return jsonify(data), 201

@main.route('/about_me', methods=['POST', 'GET'])
def about_me():
    json_data = {
        "Name": "",
        "Course": "",
        "Year": "",
        "CCAs": []
    }
    if request.method == "POST":
        json_data = request.get_json()

        name = json_data['name']
        course = json_data['course']
        year = json_data['year']
        ccas = json_data['ccas']

        collection.insert_one(json_data)

        return jsonify({'Name': name, 'Course': course, 'Year': year, 'CCAs': ccas}), 201
    
    if request.method == "GET":
        return jsonify(json_data), 201

# @main.route('/add_item', methods=['POST'])
# def add_item():
#     try:
#         if request.method == "POST":
#             print("Received POST Request")
#             return "Done", 201 
#     except Exception as e:
#         print(f"Error : {e}") 
#     return "Can't add", 404

