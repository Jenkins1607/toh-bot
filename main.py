from handlers.photos_handler import photo_router
import logg.log_config as log_config
import logging
import os 
import asyncio
from dotenv import load_dotenv
from aiogram import (
    Bot,
    Router,
    Dispatcher
)
from aiogram.filters import CommandStart
from aiogram.types import Message

logger = logging.getLogger(__name__)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmdStart(message: Message) -> None:
    """
    Отправляет приветственное сообщение в чат в ответ на /start.
    message: Message - сообщение в чате от юзера.
    """
    username = message.from_user.username
    welcome_str = f"Привет, {username}, жду новых приказаний!" 

    await message.answer(welcome_str)

async def initializeBot() -> Bot:
    """
    Загружает переменные окружения,
    инициализирует бота.
    """
    try:
        # загружаем переменные из .env
        load_dotenv() 
    
        # вытаскиваем токен из переменной окружения
        BOT_TOKEN = os.getenv("BOT_TOKEN")
        
        # инициализация экземпляра бота 
        bot = Bot(BOT_TOKEN)

        logger.info("Telegram-bot успешно инициализирован!")
    except Exception as e:
        logger.error("Ошибка инициализации бота: {e}")

    return bot

async def includeRouters(*args: Router) -> None:
    """
    Добавляет роутер в диспетчер.
    """
    try:
        dp.include_routers(*args)
        logger.info("Все роутеры подключены")
    except Exception as e:
        logger.error(f"Ошибка при подключении роутеров: {e}")


async def main() -> None:
    """
    Точка входа.

    Устанавливает логгер,
    добавляет роутеры,
    и запускает polling.
    """
    await includeRouters(photo_router)
    bot = await initializeBot()
    log_config.setupLogger()
    # начинаем опрос
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())