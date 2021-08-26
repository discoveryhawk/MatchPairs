import traceback

from db_utils import *
from exceptions import *
from markups import *
from misc import dp
from utils import get_formatted_time


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    # noinspection PyBroadException
    try:
        user = await get_user(message.from_user.id)
        if not user:
            user = await create_user(message.from_user.id, message.from_user.username, message.from_user.full_name)
        matrix = await create_empty_matrix(user)
        await fill_matrix_random_emojis(matrix)
        await message.answer(
            text='Привіт! Почнемо гру!',
            reply_markup=await get_inline_keyboard_matrix(matrix)
        )
    except Exception:
        await send_error(traceback.format_exc())


@dp.message_handler(commands=['statistics'], state='*')
async def statistics(message: types.Message):
    # noinspection PyBroadException
    try:
        await message.answer('\n'.join(
            [f"{user.fullname}: {await get_formatted_time(user.best_time)}" for user in await get_top_10_users()])
        )
    except Exception:
        await send_error(traceback.format_exc())
