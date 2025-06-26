from flask import request, jsonify
from sqlalchemy.orm import Session
from models.product import Product
from models.user import User
from models.notification import Notification
from database import get_db
from dependencies import get_current_user
from utils.helpers import save_base64_image
from config import API_URL
import uuid

def get_products(db):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('limit', 10, type=int)
    search_query = request.args.get('search', None)
    
    result = Product.get_all(db, page, per_page, search_query)
    return jsonify(result)

def get_product(product_id: str, db):
    product = Product.get_by_id(db, product_id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'error': 'Product not found'}), 404

def create_product(db, current_user):
    if not current_user:
        return jsonify({'error': 'Authentication required'}), 401

    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'price']):
        return jsonify({'error': 'Missing required fields'}), 400

    new_product = Product.create(
        db=db,
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        image_url=data.get('image_url', ''),
        created_by=current_user.id
    )
    
    # Create a notification for the new product
    notification_message = f'New product "{data["name"]}" has been added to the catalog.'
    Notification.create(db=db, message=notification_message)
    
    return jsonify(new_product.to_dict()), 201

def upload_image(current_user):
    """Upload image from base64 data"""
    if not current_user:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    
    if not data or 'image_data' not in data:
        return jsonify({'error': 'Image data is required'}), 400
    
    filename = f"{uuid.uuid4()}.jpg"
    
    filepath = save_base64_image(data['image_data'], filename)
    
    if filepath:
        image_url = f"{API_URL}/images/{filename}" 
        return jsonify({
            'message': 'Image uploaded successfully',
            'image_url': image_url,
            'filename': filename
        }), 200
    else:
        return jsonify({'error': 'Failed to save image'}), 500 