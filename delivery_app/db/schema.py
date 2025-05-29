from typing import Optional
from delivery_app.db.models import StatusChoices
from pydantic import BaseModel
from datetime import datetime


class UserProfileSchema(BaseModel):
    id:int
    first_name:str
    last_name:str
    username:str
    password:str
    phone_number:Optional[str]
    profile_image:Optional[str]
    age:Optional[int]
    status:StatusChoices
    date_register:datetime

class PhoneSchema(BaseModel):
    id:int
    rating:float
    num_ratings:int
    ram:int
    rom:int
    battery:int
    processor:str
    front_cam:float
    price_inr:int
