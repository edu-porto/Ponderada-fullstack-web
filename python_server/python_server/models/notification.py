import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message = Column(String, nullable=False)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': str(self.id),
            'message': self.message,
            'read': self.read,
            'created_at': self.created_at.isoformat()
        }

    @staticmethod
    def get_all(db):
        return db.query(Notification).order_by(Notification.created_at.desc()).all()
    
    @staticmethod
    def create(db, message):
        new_notification = Notification(message=message)
        db.add(new_notification)
        db.commit()
        db.refresh(new_notification)
        return new_notification

    @staticmethod
    def mark_as_read(db, notification_id):
        notification = db.query(Notification).filter(Notification.id == notification_id).first()
        if notification:
            notification.read = True
            db.commit()
            db.refresh(notification)
        return notification 