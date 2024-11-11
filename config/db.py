from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None
    
mongodb = MongoDB()

async def connect_to_mongo():
    try:
        mongodb.client = AsyncIOMotorClient(settings.MONGODB_URI)
        mongodb.db = mongodb.client[settings.MONGODB_DATABASE]
        await mongodb.db.command("ping")
        logger.info("Koneksi ke Database Berhasil..!!!!")
    except Exception as e:          
        logger.error("Gagal koneksi ke database karena :", e)

async def close_mongo_connection():
    if mongodb.client:
        await mongodb.client.close()
        logger.info("MongoDB connection closed.")


