from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)

@app.route('/api/spec')
def spec():
    return jsonify(swagger(app))