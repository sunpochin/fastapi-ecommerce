from sqlalchemy.engine import result
from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
    # return db.query(models.Item.delete())


# https://groups.google.com/g/sqlalchemy/c/c-qE9-KmVp8?pli=1
# https://www.navicat.com/cht/company/aboutus/blog/1745-using-the-sql-count-function-with-group-by.html

# SELECT product_id, COUNT(*) from items GROUP BY product_id;
def get_cate(db: Session, skip: int = 0, limit: int = 100):
    subs = db.query(models.Item.product_id, func.count(models.Item.product_id)).group_by(models.Item.product_id)
    return subs


def delete_all_items(db: Session, skip: int = 0, limit: int = 100):
    num = db.query(models.Item).delete()
    db.commit()
    

def delete_item(db: Session, item_id: int = -1):
    num = db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
    return num


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

def get_item_cnt(db: Session, item_id):
    return 1
    # xx = db.query(models.Item).filter(models.Item.id == item_id)
    # print('xx: ', xx)


def get_items_by_product(db: Session, product_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.product_id == product_id).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict(), owner_id=-1)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def add_item(db: Session, item_id: int):
    # , item: schemas.ItemCreate
    num = db.query(models.Item).filter(models.Item.id ==
        item_id).update({'quantity': models.Item + 1})
    return num


def decrease_item(db: Session, item_id: int):
    num = db.query(models.Item).filter(models.Item.id == item_id).update({'quantity': models.Item + 1})
    return num



