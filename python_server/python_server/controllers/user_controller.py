from flask import request, jsonify
from sqlalchemy.orm import Session
from models.user import User
from database import get_db
from dependencies import get_current_user

def get_profile(current_user):
    if not current_user:
        return jsonify({'error': 'Authentication required'}), 401
    return jsonify(current_user.to_dict())

def update_profile(db, current_user):
    if not current_user:
        return jsonify({'error': 'Authentication required'}), 401

    data = request.get_json()
    
    # Exclude password from general update, handle it separately
    if 'password' in data:
        del data['password']

    updated_user = User.update(db, current_user.id, data)

    if updated_user:
        return jsonify(updated_user.to_dict())
    
    return jsonify({'error': 'User not found'}), 404 