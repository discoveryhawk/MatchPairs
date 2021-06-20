import random

from models import Matrix, MatrixItem, session


async def create_empty_matrix(user) -> Matrix:
    matrix = Matrix(user=user)
    session.add(matrix)
    session.commit()
    return matrix


async def fill_matrix_random_emojis(matrix: Matrix):
    # emojis = '😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚'
    emojis = '☮✝☪🕉☸✡🔯🕎☯☦🛐⛎♈♉♊♋♌♍'
    emojis_and_counts = dict([(f'{emojis[i]}', 2) for i in range(18)])
    for row in range(6):
        for column in range(6):
            emoji = random.choice(list(emojis_and_counts.keys()))
            session.add(MatrixItem(row=row, column=column, value=emoji, matrix=matrix))
            emojis_and_counts[emoji] -= 1
            if emojis_and_counts[emoji] == 0:
                emojis_and_counts.pop(emoji)
    session.commit()


async def get_matrix_item(matrix_item_id):
    return session.query(MatrixItem).filter_by(id=matrix_item_id).first()


async def set_matrix_item_is_hide(matrix_item, is_hide):
    matrix_item.is_hide = is_hide
    session.add(matrix_item)
    session.commit()


async def set_matrix_item_done(matrix_item):
    matrix_item.is_done = True
    session.add(matrix_item)
    session.commit()
