"""
Модуль приема фотографий 
из чата.
"""
from models.photo import PhotoModel
from typing import Any
from utils.json_converter import Jsonator
from aiogram.types import (
    Message, 
    PhotoSize 
)
from aiogram import (
    F,
    Router
)

photo_router = Router()

@photo_router.message(F.photo)
async def handlePhoto(message: Message) -> None:
    """
    Принимает фото и отправляет на json'изацию
    """
    jsonator = Jsonator()
    # message.photo возвращает list[PhotoSize],
    # где последний элемент - фото наилучшего качества
    best_photo: PhotoSize = message.photo[-1]
    
    validate_photo = await jsonator.validate(
        model=PhotoModel, 
        model_to_validate=best_photo
        )
    if validate_photo is None:
        await message.answer("Фото не прошло проверку, попробуйте другое.")
        return 
    
    best_photo_dict: dict[str, Any] = await jsonator.toJson(best_photo)
    
    await message.answer("Фото принял, перевел экземпляр в json")
    
    
