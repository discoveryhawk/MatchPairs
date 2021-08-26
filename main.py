import traceback

from aiogram import executor

# noinspection PyUnresolvedReferences
import callbacks
# noinspection PyUnresolvedReferences
import handlers
from misc import dp

if __name__ == "__main__":
    while True:
        # noinspection PyBroadException
        try:
            executor.start_polling(dp)
        except Exception:
            print('Catch exception in MAIN:\n' + traceback.format_exc())
