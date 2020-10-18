import logging

from aiogram import Dispatcher

from data.config import owners


async def on_startup_notify(dp: Dispatcher):
    for owner in owners:
        try:
            await dp.bot.send_message(owner, "Бот Запущен и готов к работе")
        except Exception as err:
            logging.exception(err)
