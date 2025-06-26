import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from database import Base
from utils.helpers import hash_password

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(String, nullable=True)
    profile_image = Column(String, nullable=True, default='https://picsum.photos/150/150?random=default')
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'profile_image': self.profile_image,
            'created_at': self.created_at.isoformat()
        }

    @staticmethod
    def get_all(db):
        return db.query(User).all()

    @staticmethod
    def get_by_email(db, email):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_id(db, user_id):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db, name, email, password, phone, profile_image):
        hashed_pw = hash_password(password)
        new_user = User(
            name=name, 
            email=email, 
            password=hashed_pw, 
            phone=phone, 
            profile_image=profile_image
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def update(db, user_id, data):
        user = User.get_by_id(db, user_id)
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
        return user 