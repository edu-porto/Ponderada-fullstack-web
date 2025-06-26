from flask import Flask, send_from_directory
from flask_cors import CORS
import os

from config import IMAGES_DIR
from routes.auth import auth_bp
from routes.product import product_bp
from routes.user import user_bp
from routes.notification import notification_bp
from utils.data_initializer import create_tables, initialize_sample_data

# Create tables and initialize data
create_tables()
initialize_sample_data()

# Create Flask app
app = Flask(__name__)
CORS(app)

# Create images directory if it doesn't exist
os.makedirs(IMAGES_DIR, exist_ok=True)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(notification_bp, url_prefix='/api')

# Serve uploaded images
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGES_DIR, filename)

# Health check endpoint
@app.route('/')
def health_check():
    return "OK"

if __name__ == '__main__':
    # In Docker, bind to all interfaces and use port 5000 (nginx will proxy from 80)
    app.run(debug=False, host='0.0.0.0', port=5000)

