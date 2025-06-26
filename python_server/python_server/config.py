import os

# Get the absolute path of the directory where this file is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define paths for images, the only remaining file-based storage
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

# Define paths for data files
DATA_DIR = os.path.join(BASE_DIR, 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.json')
SESSIONS_FILE = os.path.join(DATA_DIR, 'sessions.json')
NOTIFICATIONS_FILE = os.path.join(DATA_DIR, 'notifications.json')

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL')

# Secret key for JWT
SECRET_KEY = os.environ.get('SECRET_KEY', 'a-very-secret-key')

# API URL
API_URL = os.environ.get('API_URL', 'http://localhost:5000') 