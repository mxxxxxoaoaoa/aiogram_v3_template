from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from app import msgs

import asyncio

router = Router()

async def func(message: Message, command: CommandObject):
    await message.answer('q')


@router.message(Command(commands = ['start', 's']))
async def wrapper(message, command):
    await asyncio.create_task(func(message, command))


