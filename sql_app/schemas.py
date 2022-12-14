from typing import List, Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    product_id: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    description: Union[str, None] = None
    quantity: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
