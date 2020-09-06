from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_unknown(message: types.Message):
    text = f"Привет, {message.from_user.full_name}!\n\nНе распознал действие, попробуй ещё раз."
    await message.answer(text)
