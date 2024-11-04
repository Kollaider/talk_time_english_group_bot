import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import BOT_TOKEN
from tkq import broker, my_task

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command("task"))
async def message(message: types.Message):
    print(message.chat.id)
    await my_task.kiq(message.chat.id)


@dp.startup()
async def setup_taskiq(bot: Bot, *_args, **_kwargs):
    if not broker.is_worker_process:
        logging.info("Setting up taskiq")
        await broker.startup()


@dp.shutdown()
async def shutdown_taskiq(bot: Bot, *_args, **_kwargs):
    if not broker.is_worker_process:
        logging.info("Shutting down taskiq")
        await broker.shutdown()


@dp.message()
async def echo_handler(message: Message) -> None:
    print(message.chat.type)
    try:
        await message.answer(message.text)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


@dp.inline_query()
async def chat_handler(message: Message) -> None:
    print(message.chat.type)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())
