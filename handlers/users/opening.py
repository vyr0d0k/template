from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command, ChatTypeFilter
from aiogram.types import Message, ChatType

from loader import dp
from utils.db_api import commands
from utils.misc import rate_limit


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), Command("reset_state"), state="*")
async def bot_reset(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Ваше состояние сброшено.")


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), CommandStart())
async def bot_start(message: Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    mention = message.from_user.get_mention()

    await commands.add_user(user_id, full_name, mention)
    await message.answer(f'Привет, <b><i>{message.from_user.full_name}</i></b>!')


@rate_limit(5, 'help')
@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), CommandHelp())
async def user_help(message: Message):
    text = [
        'Список комманд:\n',
        '/start — Начать диалог',
        '/help — Получить справку',
        '/reset_state — Нажми, если что-то пошло не так'
    ]
    await message.answer("\n".join(text))
