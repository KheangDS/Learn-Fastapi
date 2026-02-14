from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user,auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


## we don't need this line because we are using alembic to handle the database migrations
# models.Base.metadata.create_all(bind=engine)  # create the database tables

app = FastAPI() 

# origins = ["https://play.google.com"] # list of allowed origins for CORS

origins = ["*"]

app.add_middleware(
    CORSMiddleware, # Middleware : function that runs before every request and after every response
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# set up the routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message" : " Hello OunOun!"} 


