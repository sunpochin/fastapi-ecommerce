# coding=UTF-8

from datetime import date

import sql_app.models
from sql_app.database import engine, SessionLocal
from sql_app.models import Item

sql_app.models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(Item).count() == 0:
    items = [
        Item(title='夾克', product_id='1001', quantity=2),
        Item(title='拉麵之刃 T-shirt', product_id='1002'),
        Item(title='Crop top', product_id='1003'),
        Item(title='瑜伽褲', product_id='1004'),
    ]

    for item in items:
        db.add(item)

    db.commit()
