from flask import request, jsonify
from sqlalchemy.orm import Session
from models.user import User
from database import get_db
from utils.helpers import hash_password, create_jwt

def register(db):
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400

    if User.get_by_email(db, data['email']):
        return jsonify({'error': 'Email already registered'}), 400

    user = User.create(
        db=db,
        name=data['name'],
        email=data['email'],
        password=data['password'],
        phone=data.get('phone', ''),
        profile_image=data.get('profile_image', '')
    )

    return jsonify({
        'message': 'User registered successfully',
        'user': user.to_dict()
    }), 201

def login(db):
    data = request.get_json()
    if not data or not all(k in data for k in ['email', 'password']):
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.get_by_email(db, data['email'])

    if not user or user.password != hash_password(data['password']):
        return jsonify({'error': 'Invalid email or password'}), 401

    token = create_jwt(user.id)

    return jsonify({
        'message': 'Login successful',
        'token': token,
        'user': user.to_dict()
    }), 200

def logout():
    # Logout is now a client-side action (e.g., deleting the token)
    return jsonify({'message': 'Logout successful. Please clear your token.'}), 200

def reset_password():
    # This remains a simulation
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    return jsonify({'message': 'Password reset link sent (simulation)'}), 200 