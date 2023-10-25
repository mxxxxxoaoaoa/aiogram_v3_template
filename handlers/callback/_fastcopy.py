from aiogram import Router, F
from aiogram.types import CallbackQuery
from app import msgs

import asyncio

router = Router()


async def func(cq: CallbackQuery):
    pass



# @router.callback_query(F.text.lower() == "")
# @router.callback_query("" in F.text.lower())
@router.callback_query(F.text.lower().startswith(""))
async def wrapper(cq):
    await asyncio.create_task(func(cq))
