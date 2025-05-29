from fastapi import status
from fastapi import Depends,HTTPException
from delivery_app.db.models import UserProfile,Phone,RefreshToken
from delivery_app.db.schema import UserProfileSchema,PhoneSchema
from delivery_app.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List,Optional
import uvicorn
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import  OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI
from delivery_app.api import phone,user
# from delivery_app.admin.setup import setup
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter


async def init_redis():
    return redis.Redis.from_url('redis://localhost',encoding='utf-8',decode_responses=True)


@asynccontextmanager
async def lifespan(app:FastAPI):
    redis = await  init_redis()
    await FastAPILimiter.init(redis)
    yield
    await redis.close()

delivery_app = FastAPI(title='Phone', lifespan=lifespan)


delivery_app.include_router(phone.phone_router)
delivery_app.include_router(user.auth_router)



if __name__ == '__main__':
    uvicorn.run(delivery_app,host='127.0.0.2')
