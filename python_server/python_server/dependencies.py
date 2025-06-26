from flask import request, jsonify
from sqlalchemy.orm import Session
from database import get_db
from utils.helpers import decode_jwt
from models.user import User

def get_current_user(db):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return None

    token = auth_header.split(' ')[1]
    user_id = decode_jwt(token)
    
    if not user_id:
        return None
        
    user = User.get_by_id(db, user_id)
    return user 