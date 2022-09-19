# main.py

from uvicorn.config import LOGGING_CONFIG
import uvicorn
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func

from . import crud, models, schemas
from .database import SessionLocal, engine
import logging
logger = logging.getLogger("api")


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://vue2-ecommerce.netlify.app",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root(db: Session = Depends(get_db)):
    return 'set 19 15:44'


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    logger.error("len(items)", len(items))
    return items


@app.get("/items/cate")
def get_items(db: Session = Depends(get_db)):
    items = crud.get_cate(db)
    return items


@app.get("/items/get/{product_id}")
def get_items_by_product(db: Session = Depends(get_db), product_id: str = "-1", skip: int = 0, limit: int = 100):
    items = crud.get_items_by_product(db, product_id=product_id)
    logger.error("len(items)", len(items))
    return len(items)


# @app.post("/items/add", response_model=schemas.Item)
# def add_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     logger.error("item: ", item.product_id)
#     ret = crud.get_or_create(db=db, item=item)
#     return ret


@app.post("/items/add", response_model=schemas.Item)
def add_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    logger.error("items/add: ", item)
    return crud.get_or_create(db=db, item=item)
    return crud.create_item(db=db, item=item)


@app.get("/items/decrease/{product_id}")
def decrease_item(product_id: str, db: Session = Depends(get_db)):
    item = crud.decrease_item(db=db, product_id=product_id)
    return item


@app.get("/items/deleteall")
def delete_all_items(db: Session = Depends(get_db)):
    items = crud.delete_all_items(db)
    return items


# https://stackoverflow.com/questions/63809553/how-to-run-fastapi-application-from -poetry

def start():
    """Launched with `poetry run start` at root level"""
    # https: // github.com/tiangolo/fastapi/issues/1508
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    uvicorn.run("sql_app.main:app", host="0.0.0.0",
                port=8000, reload=True, log_config=log_config, )
