"""
Модуль настройки логов
(Необходимо перейти на Graylog или аналоги)
"""
import logging
import sys

def setupLogger() -> None:
    """
    Настройка конфигурации логгирования.
    """
    logging.basicConfig(
        level=logging.INFO,  # Минимальный уровень логов для записи (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s [%(levelname)s] %(message)s",  # Формат: Время [Уровень] Сообщение
        handlers=[
            logging.FileHandler("bot.log", encoding="utf-8"),  # Запись в файл
            logging.StreamHandler()                            # Вывод в консоль терминала
        ]
    )

    
