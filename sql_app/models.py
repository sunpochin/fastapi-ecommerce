from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String(255), index=True)
    title = Column(String(255), index=True)
    # description = Column(String, index=True)
    price = Column(String(255), index=True)
    quantity = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.user_id"))

    owner = relationship("User", back_populates="items")