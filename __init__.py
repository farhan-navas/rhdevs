from flask import Flask
from flask_cors import CORS
from main_routes import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wtfThisIsHard'
    CORS(app)

    app.register_blueprint(main)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
