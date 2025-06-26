from flask import Blueprint
from controllers import notification_controller
from database import get_db
from dependencies import get_current_user

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/notifications', methods=['GET'])
def get_notifications():
    db_session = next(get_db())
    current_user = get_current_user(db=db_session)
    return notification_controller.get_notifications(db=db_session, current_user=current_user)

@notification_bp.route('/notifications/<notification_id>/read', methods=['PUT'])
def mark_notification_read(notification_id):
    db_session = next(get_db())
    current_user = get_current_user(db=db_session)
    return notification_controller.mark_notification_read(notification_id=notification_id, db=db_session, current_user=current_user) 