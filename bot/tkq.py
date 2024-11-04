import asyncio
import logging

import taskiq_aiogram
from aiogram import Bot
from taskiq import TaskiqDepends, TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_redis import ListQueueBroker

from config import CHAT_ID
from util import get_meme_url

broker = ListQueueBroker("redis://redis:6379/0")

taskiq_aiogram.init(
    broker,
    "main:dp",
    "main:bot",
)

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


# @broker.task(schedule=[{"cron": "0 10 * * 1-5", "args": [1]}])
@broker.task(schedule=[{"cron": "*/1 * * * *", "args": [1]}])  # every minute
async def heavy_task(value: int, bot: Bot = TaskiqDepends()):
    meme_url = await get_meme_url()
    await bot.send_photo(chat_id=CHAT_ID, photo=meme_url)
    logging.info("Meme sent")


@broker.task(task_name="my_task")
async def my_task(chat_id: int, bot: Bot = TaskiqDepends()) -> None:
    print('2' * 100)
    print(chat_id)
    print("I'm a task")
    await asyncio.sleep(1)
    await bot.send_message(chat_id, "task completed")
