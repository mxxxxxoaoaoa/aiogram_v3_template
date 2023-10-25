from .message import start, send_kb
from aiogram import Dispatcher

class HandlerLoader:
    def __init__(self, dp: Dispatcher):
        dp.include_routers(
            start.router,
            send_kb.router
        )