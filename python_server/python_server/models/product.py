import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    creator = relationship("User")

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_url': self.image_url,
            'created_at': self.created_at.isoformat(),
            'created_by': str(self.created_by)
        }

    @staticmethod
    def get_all(db, page=1, per_page=10, search_query=None):
        query = db.query(Product)
        if search_query:
            query = query.filter(Product.name.ilike(f"%{search_query}%"))
        
        total = query.count()
        products = query.offset((page - 1) * per_page).limit(per_page).all()
        
        return {
            "products": [p.to_dict() for p in products],
            "total": total,
            "pages": (total + per_page - 1) // per_page
        }

    @staticmethod
    def get_by_id(db, product_id):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def create(db, name, description, price, image_url, created_by):
        new_product = Product(
            name=name,
            description=description,
            price=price,
            image_url=image_url,
            created_by=created_by
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product 