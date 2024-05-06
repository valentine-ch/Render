from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import aiohttp
import dotenv
import os


dotenv.load_dotenv()


ADDRESS = os.getenv("ADDRESS")
app = FastAPI()
scheduler = AsyncIOScheduler()


async def send_request():
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=f"{ADDRESS}/ping")


@app.on_event("startup")
async def startup():
    scheduler.add_job(send_request, "interval", minutes=2)
    scheduler.start()


@app.get("/ping")
async def ping():
    return "pong"
