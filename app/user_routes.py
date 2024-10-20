from flask import Blueprint, request , jsonify
from app.models import createUser, findUser
from app.utils import validate_user_data

user_bp = Blueprint('user', __name__)

@user_bp.route('/create', methods=['POST'])
def add_user():

    data = request.get_json()
    #print(data)
    if not validate_user_data(data):
        return jsonify({"message": "Invalid data", "statusCode": 400}), 400
    
    # email is the unique id
    if findUser(data['email']):
        return jsonify({"message": "User already exists", "statusCode": 400}), 400
    
    createUser(data)
    return jsonify({"message": "User created successfully", "statusCode": 201}), 201


@user_bp.route('/<username>/getDetail', methods=['POST'])
def getUserDetails(username):
    try:
        # data should contain email
        data = request.get_json(silent=True)
        
        if not data or 'email' not in data:
            return jsonify({"message": "Invalid data", "statusCode": 400}), 400
        
        res = findUser(data['email'])
        if res:
            res['statusCode'] = 200
            return jsonify(res), 200
        else:
            return jsonify({"message": "User not found", "statusCode": 404}), 404
        
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "statusCode": 500}), 500