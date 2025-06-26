from flask import Blueprint
from controllers import user_controller
from database import get_db
from dependencies import get_current_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile', methods=['GET'])
def get_profile():
    db_session = next(get_db())
    current_user = get_current_user(db=db_session)
    return user_controller.get_profile(current_user=current_user)

@user_bp.route('/profile', methods=['PUT'])
def update_profile():
    db_session = next(get_db())
    current_user = get_current_user(db=db_session)
    return user_controller.update_profile(db=db_session, current_user=current_user) 