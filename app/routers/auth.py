from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    # prefix="/auth", # add a prefix to all routes in this router, so we don't have to repeat it for each route
    tags=["Authentication"] # add tags to group the routes in the documentation
)

@router.post("/login", response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    """
    Using OAuth2PasswordRequestForm(fastapi buildin func) :
    to get the username and password from the request body, 
    which is a standard way to send credentials in a login request. 
    Now we request as a form data not as a json format
    
    """
    
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    
    # create token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    print(user.id)
    print(user.email)
    
    return {"access_token": access_token, "token_type": "bearer"}