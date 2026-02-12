# Pydantic model

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal, Optional


# receive request
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass  # Inherit all attributes from PostBase

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True

# send response(this model is used to define the response format, it can be different from the request model)
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut # to include the user details in the post response
    
    class Config:
        from_attributes = True  
"""
tells Pydantic to read data from object attributes
(like SQLAlchemy ORM models) instead of only accepting dictionaries.
"""
class PostOut(BaseModel):
    Post: Post
    votes: int
    
    class Config:
       from_attributes = True        
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]  # Only accepts 0 or 1# direction of the vote, 1 for upvote, 0 for remove vote