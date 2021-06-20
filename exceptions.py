from math import ceil

import config
from misc import bot


async def send_error(text):
    if len(text) > 4000:
        quantity_of_parts = ceil(len(text) / 4000)
        await bot.send_message(config.DeveloperId, f'ERROR. Divide message in {quantity_of_parts} parts')
        text_parts = [text[i * 4000:(i + 1) * 4000] for i in range(quantity_of_parts - 1)]
        text_parts += [text[4000 * (quantity_of_parts - 1):]]
        for text_part in text_parts:
            await bot.send_message(
                config.DeveloperId,
                text_part
            )
    else:
        await bot.send_message(
            config.DeveloperId,
            text
        )
