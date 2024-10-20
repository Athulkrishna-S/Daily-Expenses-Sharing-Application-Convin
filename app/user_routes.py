from flask import Blueprint, request , jsonify
from app.models import createUser, findUser
from app.utils import validate_user_data
from flask_jwt_extended import  create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import timedelta
from app.auth import blacklisted_tokens
user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['POST'])
def login():
    '''
    Endpoint for user login, expects email and password in the body.
    '''
    data = request.get_json()
    email = data.get('email')
    mobile = data.get('mobile')
    username = data.get('name')

    if not validate_user_data(data):
        return jsonify({"message": "Invalid data", "statusCode": 400}), 400
    
    # Find the user by email
    user = findUser(email)

    if not user:
        return jsonify({"message": "User not found", "statusCode": 404}), 404

    user_identity = {"username": username, "email": email}

    # Generate the JWT token
    expires = timedelta(minutes=120)
    access_token = create_access_token(identity=user_identity, expires_delta=expires)
    
   
    return jsonify({"token": access_token, "statusCode": 200}), 200

@user_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():

    jti = get_jwt()['jti']  # Get the unique identifier for the token
    blacklisted_tokens.add(jti)  # Blacklist the token
    return jsonify({"msg": "Successfully logged out"}), 200



@user_bp.route('/create', methods=['POST'])
def add_user():

    data = request.get_json()
   
    if not validate_user_data(data):
        return jsonify({"message": "Invalid data", "statusCode": 400}), 400
    
    # email is the unique id
    if findUser(data['email']):
        return jsonify({"message": "User already exists", "statusCode": 400}), 400
    
    createUser(data)
    return jsonify({"message": "User created successfully", "statusCode": 201}), 201


# This endpoint allows authenticated users to access their own details only.
@user_bp.route('/getDetail', methods=['GET'])
@jwt_required()
def getUserDetails():
    try:
            
        data = get_jwt_identity()

        
        
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