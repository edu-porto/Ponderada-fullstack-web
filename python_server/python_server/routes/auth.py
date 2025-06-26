from flask import Blueprint, request
from controllers import auth_controller
from database import get_db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return auth_controller.register(db=next(get_db()))

@auth_bp.route('/login', methods=['POST'])
def login():
    return auth_controller.login(db=next(get_db()))

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return auth_controller.logout()

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    return auth_controller.reset_password() 