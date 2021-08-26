import traceback

from aiogram import types
from aiogram.dispatcher import FSMContext

from exceptions import send_error
from misc import dp


@dp.message_handler(content_types=types.ContentTypes.ANY, state='*')
async def all_other_messages(message: types.Message, state: FSMContext):
    try:
        await message.answer(
            text='Користуйтесь кнопками'
        )
    except Exception:
        await send_error(traceback.format_exc())
