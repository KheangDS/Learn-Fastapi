from fastapi import APIRouter, Depends, status, HTTPException, Response, FastAPI
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2, database
from ..database import get_db

router = APIRouter(
    prefix="/vote",
    tags=["Votes"]
)
@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # check if the post exists
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist")
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first() # check if it's composite primary key, so only one record per user per post
    
    if (vote.dir == 1):
        if found_vote:
            # if the user has already voted on the post, we cannot allow them to vote again, so we raise a conflict error
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote does not exist")
        
        # if the user has voted on the post and wants to remove their vote, we delete the vote record from the database
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully deleted vote"}