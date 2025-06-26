from models.user import User
from models.product import Product
from models.notification import Notification
from database import SessionLocal, engine, Base
import uuid
from datetime import datetime, timedelta

def create_tables():
    Base.metadata.create_all(bind=engine)

def initialize_sample_data():
    """Initialize with sample products and users"""
    db = SessionLocal()
    
    # Check if data already exists
    if db.query(User).first() or db.query(Product).first():
        db.close()
        return

    # Sample admin user
    admin_user = User.create(
        db=db,
        name='Admin User',
        email='admin@example.com',
        password='admin123',
        phone='+1234567890',
        profile_image='https://picsum.photos/150/150?random=admin'
    )

    # Sample products
    for i in range(1, 101):
        Product.create(
            db=db,
            name=f'Product {i}',
            description=f'This is a sample product {i} with detailed description.',
            price=round(10.99 + (i * 2.5), 2),
            image_url=f'https://picsum.photos/300/300?random={i}',
            created_by=admin_user.id
        )
    
    # Sample notifications
    sample_notifications = [
        'Welcome to Product App! Your account has been created successfully.',
        'New product "Product 50" has been added to the catalog.',
        'Your profile has been updated successfully.',
        'System maintenance scheduled for tomorrow at 2 AM.',
        'You have 5 new products in your catalog.',
        'Don\'t forget to check out the latest features!'
    ]
    
    for message in sample_notifications:
        Notification.create(
            db=db,
            message=message
        )
    
    db.close() 