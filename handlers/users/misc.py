from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp


# @dp.message_handler(Command("test"), state="*")
# async def test_func(message: types.Message):


@dp.message_handler(Command("reset"), state="*")
async def bot_reset(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Ваше состояние сброшено.")


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_unknown(message: types.Message):
    text = f"Привет, <b><i>{message.from_user.full_name}</i></b>!\n\nНе распознал действие, попробуй ещё раз."
    await message.answer(text)
