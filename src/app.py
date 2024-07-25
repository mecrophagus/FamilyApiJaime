"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


# Create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET', 'POST'])
def handle_family_members():
    # This is how you can use the Family datastructure by calling its methods
    response_body = {}
    members = jackson_family.get_all_members()
    if request.method == 'GET':
       response_body = { "hello": "world",
                      "family": members}
    return response_body, 200
    if request.method == 'POST':
       data = request.json
       members.append(data)
       response_body['results'] = members
    return response_body, 200


@app.route('/members/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_family_member(member_id):
    response_body = {}
    if member_id >= len(members):
        response_body['message'] = 'That member is not even born yet'
        response_body['results'] = {}
        return response_body, 404
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.methos == 'DELETE':
        pass


# This only runs if `$ python src/app.py` is executed


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
