import nest_asyncio
nest_asyncio.apply()

# aiogram imports
from aiogram import Bot, Dispatcher, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

# yours imports
from config import load_config
from database import db as datab
from data import messages

# python libs imports
import logging
import asyncio

msgs = messages.load_messages()
config = load_config('.env')
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format=u'%(levelname)-1s [%(asctime)s] - %(message)s',
    datefmt='%d.%m %H:%M',
)

bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.MARKDOWN_V2)
logger.info('INIT BOT CLASS')

db = datab.BotDatabase(config.db.filename)
logger.info('INIT DB')

async def starter():
    logger.info("STARTING BOT...")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    from handlers._loader import HandlerLoader

    HandlerLoader(dp)
    logger.info("SETUP HANDLERS")

    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("BOT STARTED.")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(starter())
