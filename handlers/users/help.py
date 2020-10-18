from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import owners
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def user_help(message: Message):
    user_id = message.from_user.id
    text = [
        'Список комманд:\n',
        '/start — Начать диалог',
        '/help — Получить справку',
        '/reset — Нажми, если что-то пошло не так'
    ]
    if user_id in owners:
        text.append('/mail — Рассылка по пользователям')
        await message.answer("\n".join(text))
    else:
        await message.answer("\n".join(text))
