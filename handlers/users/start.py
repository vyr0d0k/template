from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api import commands


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    mention = message.from_user.get_mention()

    await commands.add_user(user_id, full_name, mention)
    await message.answer(f'Привет, <b><i>{message.from_user.full_name}</i></b>!')
