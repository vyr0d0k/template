import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, ContentTypes

from data.config import owners
from loader import dp
from utils.db_api import commands


@dp.message_handler(Command("mail"), user_id=owners, state="*")
async def mailing_enter(message: Message, state: FSMContext):
    await state.set_state("mailing_enter")
    await message.answer("Отправьте то, что хотите разослать, в формате одного сообщения.")


@dp.message_handler(state="mailing_enter", content_types=ContentTypes.ANY)
async def mailing_msg(message: Message, state: FSMContext):
    self = message.from_user.id
    await state.set_state("approve_mailing")
    await message.send_copy(chat_id=self,
                            reply_markup=InlineKeyboardMarkup(
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Выполнить рассылку", callback_data="mail_approve"),
                                        InlineKeyboardButton(text="Отмена", callback_data="mail_decline")
                                    ]
                                ], row_width=2
                            ))


@dp.callback_query_handler(state="approve_mailing", text="mail_approve")
async def mailing_approve(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup()
    await state.reset_state()
    users = await commands.select_all_users()
    for user in users:
        await call.message.send_copy(user.user_id, reply_markup=InlineKeyboardMarkup())
        await asyncio.sleep(0.3)
    await call.message.answer("Рассылка завершена.")


@dp.callback_query_handler(state="approve_mailing", text="mail_decline")
async def mailing_decline(call: CallbackQuery, state: FSMContext):
    type = call.message.content_type
    await call.answer()
    await state.reset_state()
    if type == "text":
        await call.message.edit_text("Вы отменили рассылку.")
    else:
        await call.message.delete()
        await call.message.answer("Вы отменили рассылку.")
