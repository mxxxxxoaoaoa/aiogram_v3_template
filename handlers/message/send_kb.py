from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from app import msgs
from keyboards import inline

import asyncio

router = Router()


async def func(message: Message, command: CommandObject):
    args = command.args
    if args is None or int(args) > 100:
        return
    if args.isdigit():
        await message.answer("q", reply_markup=inline.int_kb(int(args)))
    else:
        await message.answer("q", reply_markup=inline.int_kb())

@router.message(Command(commands = ['int']))
async def wrapper(message, command):
    await asyncio.create_task(func(message, command))
