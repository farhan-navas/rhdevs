from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello Backend'

@app.route('/about_me')
def about_us():
    name = "Mohamed Navas Farhan"
    course = "Computer Science"
    year = "1"
    ccas = ["RH Devs", "Ultimate", "HPB", "RVC Pioneers"]
    ccas_str = ', '.join(ccas)

    return f"Name: {name} <br> Course: {course} <br> Year: {year} <br> CCA's: {ccas_str}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)