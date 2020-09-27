from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import admins, owner, moderators
from loader import dp


@dp.message_handler(Command("reset"), state="*")
async def bot_reset(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Ваше состояние сброшено.")


@dp.message_handler(Command("add_new_admin"), user_id=owner)
async def new_admin(message: types.Message, state: FSMContext):
    await message.answer("Введите ID пользователя которого хотите добавить в Администраторов:")
    await state.set_state("new_admin")


@dp.message_handler(user_id=owner, state="new_admin", regexp=r"^(/d+)$")
async def add_new_admin(message: types.Message, state: FSMContext):
    id = int(message.text)
    admins.append(id)
    await message.answer(f"Вы добавили в Администраторы пользователя с ID: {id}")
    await state.reset_state()


@dp.message_handler(Command("add_new_moderator"), user_id=admins)
async def new_moderator(message: types.Message, state: FSMContext):
    await message.answer("Введите ID пользователя которого хотите добавить в Модераторов:")
    await state.set_state("new_moderator")


@dp.message_handler(user_id=admins, state="new_moderator", regexp=r"^(/d+)$")
async def add_new_moderator(message: types.Message, state: FSMContext):
    id = int(message.text)
    moderators.append(id)
    await message.answer(f"Вы добавили в Модераторы пользователя с ID: {id}")
    await state.reset_state()


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_unknown(message: types.Message):
    text = f"Привет, <b><i>{message.from_user.full_name}</i></b>!\n\nНе распознал действие, попробуй ещё раз."
    await message.answer(text)
