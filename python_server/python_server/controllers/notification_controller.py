from flask import request, jsonify
from sqlalchemy.orm import Session
from models.notification import Notification
from models.user import User
from database import get_db
from dependencies import get_current_user

def get_notifications(db, current_user):
    if not current_user:
        return jsonify({'error': 'Authentication required'}), 401
    
    notifications = Notification.get_all(db)
    return jsonify([n.to_dict() for n in notifications])

def mark_notification_read(notification_id: str, db, current_user):
    if not current_user:
        return jsonify({'error': 'Authentication required'}), 401

    notification = Notification.mark_as_read(db, notification_id)
    if notification:
        return jsonify(notification.to_dict())
    return jsonify({'error': 'Notification not found'}), 404 