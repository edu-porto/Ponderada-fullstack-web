from flask import Blueprint
from controllers import product_controller
from database import get_db
from dependencies import get_current_user

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    return product_controller.get_products(db=next(get_db()))

@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    return product_controller.get_product(product_id=product_id, db=next(get_db()))

@product_bp.route('/products', methods=['POST'])
def create_product():
    db_session = next(get_db())
    current_user = get_current_user(db=db_session)
    return product_controller.create_product(db=db_session, current_user=current_user)

@product_bp.route('/upload-image', methods=['POST'])
def upload_image():
    db_session = next(get_db())
    current_user = get_current_user(db=db_session)
    return product_controller.upload_image(current_user=current_user) 