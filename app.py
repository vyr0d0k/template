import logging

from loader import db
from utils.db_api import db_gino
from utils.misc import setup_logger
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    import filters
    import middlewares
    filters.setup(dispatcher)
    logging.info("Filters are successfully configured")
    middlewares.setup(dispatcher)
    logging.info("Middlewares are successfully configured")

    from utils.notify_admins import on_startup_notify

    await db_gino.on_startup()
    logging.info("PostgreSQL is successfully connected")

    # await db.gino.drop_all()
    # logging.info("Database tables are successfully dropped")

    await db.gino.create_all()
    logging.info("Database tables are successfully loaded")

    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    setup_logger(['sqlalchemy.engine', 'aiogram.bot.api'])
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
