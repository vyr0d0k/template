from typing import Union

from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ContentTypes, Message, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent, ChatType

from loader import dp


@dp.inline_handler(state="*")
@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), state="*")
@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), state="*", content_types=ContentTypes.ANY)
async def unknown_update(query: Union[Message, CallbackQuery, InlineQuery]):
    if isinstance(query, Message):
        answer = f"Привет, <b><i>{query.from_user.full_name}</i></b>!\n\nНе распознал действие, попробуй ещё раз."
    elif isinstance(query, CallbackQuery):
        answer = "Не зарегистрированное действие"
    else:
        answer = [InlineQueryResultArticle(
            id="unknown_query", title="Неизвестный запрос",
            input_message_content=InputTextMessageContent("Сказано же, <b>неизвестный</b> запрос"))]
    await query.answer(answer)
