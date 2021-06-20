import asyncio
import datetime
import traceback

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from db_utils import *
from exceptions import send_error
from markups import *
from misc import dp
from utils import get_formatted_time


@dp.callback_query_handler(lambda call: 'choice' == call.data.split('#')[0], state='*')
async def choice(call: CallbackQuery, state: FSMContext):
    # noinspection PyBroadException
    try:
        data = await state.get_data()
        matrix_item = await get_matrix_item(call.data.split('#')[1])
        if not matrix_item.is_hide:
            return await call.answer('Ви вже відкрили цю карточку!')
        await call.answer()
        matrix = matrix_item.matrix
        first_matrix_item_id = data.get('first_matrix_item_id')
        if not first_matrix_item_id:
            await set_matrix_item_is_hide(matrix_item, False)
            await state.update_data(first_matrix_item_id=matrix_item.id)
            await call.message.edit_reply_markup(await get_inline_keyboard_matrix(matrix))
        else:
            await state.reset_data()
            await set_matrix_item_is_hide(matrix_item, False)
            await call.message.edit_reply_markup(await get_inline_keyboard_matrix(matrix))
            first_matrix_item = await get_matrix_item(first_matrix_item_id)
            if matrix_item.value != first_matrix_item.value:
                await asyncio.sleep(0.5)
                await set_matrix_item_is_hide(matrix_item, True)
                await set_matrix_item_is_hide(first_matrix_item, True)
                return await call.message.edit_reply_markup(await get_inline_keyboard_matrix(matrix))
            else:
                await set_matrix_item_done(matrix_item)
                await set_matrix_item_done(first_matrix_item)
            for matrix_item in matrix.matrix_items:
                if not matrix_item.is_done:
                    return
            spent_time = datetime.datetime.now() - matrix.created
            await call.message.edit_text(
                text=f'Вітаю! Ти переміг!\nВитрачений час: {await get_formatted_time(spent_time.seconds)}',
                reply_markup=await get_inline_keyboard_matrix(matrix)
            )
            if not matrix.user.best_time or matrix.user.best_time > spent_time.seconds:
                await set_user_best_time(matrix.user, spent_time.seconds)
    except Exception:
        await send_error(traceback.format_exc())


@dp.callback_query_handler(lambda call: 'start_new_game' == call.data.split('#')[0], state='*')
async def start_new_game(call: CallbackQuery, state: FSMContext):
    # noinspection PyBroadException
    try:
        await state.reset_data()
        await call.answer()
        user = await get_user(call.from_user.id)
        matrix = await create_empty_matrix(user)
        await fill_matrix_random_emojis(matrix)
        await call.message.delete()
        await call.message.answer(text='Нова гра!', reply_markup=await get_inline_keyboard_matrix(matrix=matrix))
    except Exception:
        await send_error(traceback.format_exc())


@dp.callback_query_handler(lambda call: 'end_game' == call.data.split('#')[0], state='*')
async def end_game(call: CallbackQuery, state: FSMContext):
    # noinspection PyBroadException
    try:
        await state.reset_data()
        await call.answer()
        await call.message.delete()
    except Exception:
        await send_error(traceback.format_exc())
