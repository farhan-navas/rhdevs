from flask import Flask
from flask_cors import CORS
from main_routes import main
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://farhanmnavas:Farhanop2811$@cluster0.vmoxzj4.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wtfThisIsHard'
    CORS(app)

    app.register_blueprint(main)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
