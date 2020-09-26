from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import admins, owner, moderators
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    id = message.from_user.id
    text = [
        'Список команд:\n',
        '/start — Начать диалог',
        '/help — Получить справку',
        '/reset — Если что-то пошло не так'
    ]
    if id == owner:
        text.extend([])
        await message.answer('\n'.join(text))
    elif id in admins:
        text.extend([])
        await message.answer('\n'.join(text))
    elif id in moderators:
        text.extend([])
        await message.answer('\n'.join(text))
    else:
        text.extend([])
        await message.answer('\n'.join(text))
