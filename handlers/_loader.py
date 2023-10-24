from .message import start
from aiogram import Dispatcher

class HandlerLoader:
    def __init__(self, dp: Dispatcher):
        dp.include_routers(
            start.router
        )