import json
import os
import hashlib
import secrets
import base64
import uuid
import jwt
from datetime import datetime, timedelta
from config import (
    DATA_DIR, IMAGES_DIR, USERS_FILE, PRODUCTS_FILE, SESSIONS_FILE, NOTIFICATIONS_FILE, SECRET_KEY
)

def load_data(filename):
    """Load data from JSON file"""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(filename, data):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_session_token():
    """Generate a secure session token"""
    return secrets.token_hex(32)

def is_valid_session(token):
    """Check if session token is valid"""
    sessions = load_data(SESSIONS_FILE)
    if token in sessions:
        session = sessions[token]
        created_at = datetime.fromisoformat(session['created_at'])
        if datetime.now() - created_at < timedelta(hours=24):
            return session['user_id']
    return None

def create_jwt(user_id):
    """Create a new JWT for a user"""
    payload = {
        'sub': str(user_id),
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    """Decode and validate a JWT"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None # Signature has expired
    except jwt.InvalidTokenError:
        return None # Invalid token

def save_base64_image(base64_string, filename):
    """Save base64 encoded image to file"""
    try:
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        image_data = base64.b64decode(base64_string)
        
        filepath = os.path.join(IMAGES_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(image_data)
        
        return filepath
    except Exception as e:
        print(f"Error saving image: {e}")
        return None

def add_notification(db, message):
    """Add a new notification"""
    from models.notification import Notification
    Notification.create(db, message=message) 