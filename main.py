from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from .config.db import mongodb, connect_to_mongo, close_mongo_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to MongoDB
    await connect_to_mongo()
    yield  # Control passes to FastAPI app's request handling here
    # Shutdown: Disconnect from MongoDB
    await close_mongo_connection()
 
def get_database():
    if mongodb.db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    return mongodb.db

app = FastAPI(lifespan=lifespan)