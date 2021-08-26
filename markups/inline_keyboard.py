from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_inline_keyboard_matrix(matrix):
    inline_keyboard = InlineKeyboardMarkup(row_width=6)
    inline_keyboard.add(
        *[
            InlineKeyboardButton(
                text=f'😈' if matrix_item.is_hidden else matrix_item.value,
                callback_data=f'choice#{matrix_item.id}'
            ) for matrix_item in matrix.matrix_items
        ]
    )
    inline_keyboard.add(InlineKeyboardButton(text='Завершити гру', callback_data='end_game'))
    inline_keyboard.add(InlineKeyboardButton(text='Почати нову гру', callback_data='start_new_game'))
    return inline_keyboard
