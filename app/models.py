# This file represents every database table as a Python class
# ORM Model: Object Relational Mapping

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"  # table name in the database

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default=('TRUE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    """
    - foreign key to the users table, 
    - ondelete="CASCADE" means that if the user is deleted, all their posts will be deleted as well
    - datatype of owner_id is Integer because it references the id column in the users table which is of type Integer
    """
    owner = relationship("User") # reference to the User model, to get the user details when we query a post
    
class User(Base):
    __tablename__ = "users"  # table name in the database

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True) # unique : no duplicate emails
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Vote(Base):
    __tablename__ = "votes"  # table name in the database

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True) 
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True) 
    """
    - composite primary key (user_id, post_id) : no duplicate rows with these 2 columns , a user can only vote once for a post
    - ondelete="CASCADE" means that if the user or post is deleted, the corresponding votes will be deleted as well
    """