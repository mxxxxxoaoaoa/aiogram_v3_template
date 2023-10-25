from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from app import msgs

import asyncio

router = Router()


async def func(message: Message, command: CommandObject):
    pass


# @router.message(Command(commands = ['com']))
# @router.message(F.text == "text")
@router.message()
async def wrapper(message, command):
    await asyncio.create_task(func(message, command))
