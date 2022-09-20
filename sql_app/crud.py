from sqlalchemy.engine import result
from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas
import logging
logger = logging.getLogger("api")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    logger.error("create_user_item: ${0}".format(user_id))
    # https://myapollo.com.tw/zh-tw/sqlalchemy-filter-vs-filter-by/
    db_item = db.query(models.Item).filter(
        models.Item.product_id == item.product_id, 
        models.Item.owner_id == user_id).first()
    logger.error("db_item: %s", db_item)
    if db_item is None:
        db_item = models.Item(**item.dict(), quantity=1, owner_id=user_id)
        db.add(db_item)
        logger.error("Create new db_item: ${0}".format(user_id))
    else:
        newquan = db_item.quantity + 1
        ret = db.query(models.Item).filter(models.Item.product_id == item.product_id)\
            .update({"quantity": newquan}, synchronize_session="fetch")
        logger.error("Increase quantity db_item: ${0}".format(newquan))
    # logger.error("get_or_create db_item: ", db_item.quantity)
    db.commit()
    db.refresh(db_item)
    return db_item

    # db_item = models.Item(**item.dict(), owner_id=user_id)
    # db.add(db_item)
    # db.commit()
    # db.refresh(db_item)
    # return db_item


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
    # return db.query(models.Item.delete())


def delete_all_items(db: Session, skip: int = 0, limit: int = 100):
    num = db.query(models.Item).delete()
    db.commit()


def get_item_cnt(db: Session, item_id):
    return 1
    # xx = db.query(models.Item).filter(models.Item.id == item_id)
    # print('xx: ', xx)


def get_items_by_product(db: Session, product_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.product_id == product_id).offset(skip).limit(limit).all()


# https://groups.google.com/g/sqlalchemy/c/c-qE9-KmVp8?pli=1
# https://www.navicat.com/cht/company/aboutus/blog/1745-using-the-sql-count-function-with-group-by.html
# SELECT product_id, COUNT(*) from items GROUP BY product_id;
def get_cate(db: Session, skip: int = 0, limit: int = 100):
    # subs = db.query(models.Item.product_id, func.count(
    #     models.Item.product_id), models.Item.quantity).group_by(models.Item.product_id)
    subs = db.query(models.Item.product_id, models.Item.quantity)
    return subs


def create_item(db: Session, item: schemas.ItemCreate):
    # db_item = models.Item(**item.dict(), owner_id=-1)
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# https://groups.google.com/g/sqlalchemy/c/tVc19TUJQu8


def get_or_create(db: Session, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(
        models.Item.product_id == item.product_id).first()
    if db_item is None:
        # db_item = models.Item(**item.dict(), quantity=1, owner_id=-1)
        db_item = models.Item(**item.dict(), quantity=1)
        db.add(db_item)
        logger.error("get_or_create db_item: ", db_item)
    else:
        newquan = db_item.quantity + 1
        ret = db.query(models.Item).filter(models.Item.product_id == item.product_id)\
            .update({"quantity": newquan}, synchronize_session="fetch")
        logger.error("get_or_create db_item: ", ret)
    # logger.error("get_or_create db_item: ", db_item.quantity)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id):
    num = db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
    return num


def add_item(db: Session, item_id: int):
    # , item: schemas.ItemCreate
    num = db.query(models.Item).filter(models.Item.id ==
                                       item_id).update({'quantity': models.Item + 1})
    return num


def decrease_item(db: Session, product_id: str):
    db_item = db.query(models.Item).filter(
        models.Item.product_id == product_id).first()
    newquan = db_item.quantity - 1
    if newquan <= 0:
        # db_item.delete()
        ret = db.query(models.Item).filter(
            models.Item.product_id == product_id).delete()
        pass
    else:
        ret = db.query(models.Item).filter(
            models.Item.product_id == product_id).update({"quantity": newquan}, synchronize_session="fetch")
    db.commit()
    return newquan
