from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import hashlib
import uuid
from datetime import datetime, timedelta
import secrets
import base64

app = Flask(__name__)
CORS(app)

# Simple file-based storage
DATA_DIR = 'data'
IMAGES_DIR = 'images'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.json')
SESSIONS_FILE = os.path.join(DATA_DIR, 'sessions.json')
NOTIFICATIONS_FILE = os.path.join(DATA_DIR, 'notifications.json')

# Create data and images directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

def load_data(filename):
    """Load data from JSON file"""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
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
        # Check if session is not expired (24 hours)
        created_at = datetime.fromisoformat(session['created_at'])
        if datetime.now() - created_at < timedelta(hours=24):
            return session['user_id']
    return None

def save_base64_image(base64_string, filename):
    """Save base64 encoded image to file"""
    try:
        # Remove data URL prefix if present
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        # Decode base64 string
        image_data = base64.b64decode(base64_string)
        
        # Save to file
        filepath = os.path.join(IMAGES_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(image_data)
        
        return filepath
    except Exception as e:
        print(f"Error saving image: {e}")
        return None

# Initialize with sample data
def initialize_sample_data():
    """Initialize with sample products and users"""
    # Sample products
    products = load_data(PRODUCTS_FILE)
    if not products:
        sample_products = {}
        for i in range(1, 101):  # Create 100 sample products
            product_id = str(uuid.uuid4())
            sample_products[product_id] = {
                'id': product_id,
                'name': f'Product {i}',
                'description': f'This is a sample product {i} with detailed description.',
                'price': round(10.99 + (i * 2.5), 2),
                'image_url': f'https://picsum.photos/300/300?random={i}',
                'created_at': datetime.now().isoformat(),
                'created_by': 'system'
            }
        save_data(PRODUCTS_FILE, sample_products)
    
    # Sample admin user
    users = load_data(USERS_FILE)
    if not users:
        admin_id = str(uuid.uuid4())
        users[admin_id] = {
            'id': admin_id,
            'name': 'Admin User',
            'email': 'admin@example.com',
            'password': hash_password('admin123'),
            'phone': '+1234567890',
            'profile_image': 'https://picsum.photos/150/150?random=admin',
            'created_at': datetime.now().isoformat()
        }
        save_data(USERS_FILE, users)

# Serve uploaded images
@app.route('/images/<filename>')
def serve_image(filename):
    """Serve uploaded images"""
    return send_from_directory(IMAGES_DIR, filename)

# Image upload endpoint
@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    """Upload image from base64 data"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = is_valid_session(token)
    
    if not user_id:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    
    if not data or 'image_data' not in data:
        return jsonify({'error': 'Image data is required'}), 400
    
    # Generate unique filename
    filename = f"{uuid.uuid4()}.jpg"
    
    # Save image
    filepath = save_base64_image(data['image_data'], filename)
    
    if filepath:
        image_url = f"http://localhost:5000/images/{filename}"
        return jsonify({
            'message': 'Image uploaded successfully',
            'image_url': image_url,
            'filename': filename
        }), 200
    else:
        return jsonify({'error': 'Failed to save image'}), 500

# Authentication endpoints
@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    if not data or not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    users = load_data(USERS_FILE)
    
    # Check if email already exists
    for user in users.values():
        if user['email'] == data['email']:
            return jsonify({'error': 'Email already registered'}), 400
    
    # Create new user
    user_id = str(uuid.uuid4())
    users[user_id] = {
        'id': user_id,
        'name': data['name'],
        'email': data['email'],
        'password': hash_password(data['password']),
        'phone': data.get('phone', ''),
        'profile_image': data.get('profile_image', 'https://picsum.photos/150/150?random=default'),
        'created_at': datetime.now().isoformat()
    }
    
    save_data(USERS_FILE, users)
    
    return jsonify({
        'message': 'User registered successfully',
        'user': {
            'id': user_id,
            'name': data['name'],
            'email': data['email']
        }
    }), 201

@app.route('/api/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()
    
    if not data or not all(k in data for k in ['email', 'password']):
        return jsonify({'error': 'Missing email or password'}), 400
    
    users = load_data(USERS_FILE)
    
    # Find user by email
    user = None
    for u in users.values():
        if u['email'] == data['email']:
            user = u
            break
    
    if not user or user['password'] != hash_password(data['password']):
        return jsonify({'error': 'Invalid email or password'}), 401
    
    # Create session
    token = generate_session_token()
    sessions = load_data(SESSIONS_FILE)
    sessions[token] = {
        'user_id': user['id'],
        'created_at': datetime.now().isoformat()
    }
    save_data(SESSIONS_FILE, sessions)
    
    return jsonify({
        'message': 'Login successful',
        'token': token,
        'user': {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'phone': user.get('phone', ''),
            'profile_image': user.get('profile_image', '')
        }
    }), 200

@app.route('/api/logout', methods=['POST'])
def logout():
    """Logout user"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    if token:
        sessions = load_data(SESSIONS_FILE)
        if token in sessions:
            del sessions[token]
            save_data(SESSIONS_FILE, sessions)
    
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    """Reset password (simplified - just returns success)"""
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    users = load_data(USERS_FILE)
    
    # Check if email exists
    email_exists = any(user['email'] == data['email'] for user in users.values())
    
    if email_exists:
        # In a real app, you would send an email with reset instructions
        return jsonify({'message': 'Password reset instructions sent to your email'}), 200
    else:
        return jsonify({'error': 'Email not found'}), 404

# Product endpoints
@app.route('/api/products', methods=['GET'])
def get_products():
    """Get products with pagination"""
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    search = request.args.get('search', '')
    
    products = load_data(PRODUCTS_FILE)
    product_list = list(products.values())
    
    # Filter by search term
    if search:
        product_list = [p for p in product_list if search.lower() in p['name'].lower() or search.lower() in p['description'].lower()]
    
    # Sort by created_at (newest first)
    product_list.sort(key=lambda x: x['created_at'], reverse=True)
    
    # Pagination
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    paginated_products = product_list[start_idx:end_idx]
    
    return jsonify({
        'products': paginated_products,
        'total': len(product_list),
        'page': page,
        'limit': limit,
        'total_pages': (len(product_list) + limit - 1) // limit
    }), 200

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product by ID"""
    products = load_data(PRODUCTS_FILE)
    
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify({'product': products[product_id]}), 200

@app.route('/api/products', methods=['POST'])
def create_product():
    """Create a new product"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = is_valid_session(token)
    
    if not user_id:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    
    if not data or not all(k in data for k in ['name', 'description', 'price']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    products = load_data(PRODUCTS_FILE)
    
    product_id = str(uuid.uuid4())
    products[product_id] = {
        'id': product_id,
        'name': data['name'],
        'description': data['description'],
        'price': float(data['price']),
        'image_url': data.get('image_url', 'https://picsum.photos/300/300?random=new'),
        'created_at': datetime.now().isoformat(),
        'created_by': user_id
    }
    
    save_data(PRODUCTS_FILE, products)
    
    # Add notification for new product
    add_notification(f"New product '{data['name']}' has been added!")
    
    return jsonify({
        'message': 'Product created successfully',
        'product': products[product_id]
    }), 201

# User profile endpoints
@app.route('/api/profile', methods=['GET'])
def get_profile():
    """Get user profile"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = is_valid_session(token)
    
    if not user_id:
        return jsonify({'error': 'Authentication required'}), 401
    
    users = load_data(USERS_FILE)
    
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    user = users[user_id]
    return jsonify({
        'user': {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'phone': user.get('phone', ''),
            'profile_image': user.get('profile_image', '')
        }
    }), 200

@app.route('/api/profile', methods=['PUT'])
def update_profile():
    """Update user profile"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = is_valid_session(token)
    
    if not user_id:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    users = load_data(USERS_FILE)
    
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    # Update user data
    user = users[user_id]
    if 'name' in data:
        user['name'] = data['name']
    if 'phone' in data:
        user['phone'] = data['phone']
    if 'profile_image' in data:
        user['profile_image'] = data['profile_image']
    if 'password' in data and data['password']:
        user['password'] = hash_password(data['password'])
    
    save_data(USERS_FILE, users)
    
    return jsonify({
        'message': 'Profile updated successfully',
        'user': {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'phone': user.get('phone', ''),
            'profile_image': user.get('profile_image', '')
        }
    }), 200

# Notification endpoints
def add_notification(message):
    """Add a new notification"""
    notifications = load_data(NOTIFICATIONS_FILE)
    
    notification_id = str(uuid.uuid4())
    notifications[notification_id] = {
        'id': notification_id,
        'message': message,
        'created_at': datetime.now().isoformat(),
        'read': False
    }
    
    save_data(NOTIFICATIONS_FILE, notifications)

@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    """Get all notifications"""
    notifications = load_data(NOTIFICATIONS_FILE)
    notification_list = list(notifications.values())
    
    # Sort by created_at (newest first)
    notification_list.sort(key=lambda x: x['created_at'], reverse=True)
    
    return jsonify({'notifications': notification_list}), 200

@app.route('/api/notifications/<notification_id>/read', methods=['PUT'])
def mark_notification_read(notification_id):
    """Mark notification as read"""
    notifications = load_data(NOTIFICATIONS_FILE)
    
    if notification_id not in notifications:
        return jsonify({'error': 'Notification not found'}), 404
    
    notifications[notification_id]['read'] = True
    save_data(NOTIFICATIONS_FILE, notifications)
    
    return jsonify({'message': 'Notification marked as read'}), 200

if __name__ == '__main__':
    initialize_sample_data()
    app.run(host='0.0.0.0', port=5000, debug=True)

