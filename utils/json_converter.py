import logging
from models.photo import PhotoModel
from pydantic import (
    ValidationError,
    BaseModel
    )
from typing import Any
import json

logger = logging.getLogger(__name__)

class Jsonator:
    def __init__(self):
        pass

    async def validate(
            self,
            model: type[BaseModel],
            model_to_validate: Any
            ) -> type[BaseModel] | None:
        """
        Проверяет cоответствие модели из модуля models.

        model: type[BaseModel] - модель-эталон
        model_to_validate: Any - объект любого класса
        """
        try:
            validated_model = model.model_validate(model_to_validate)
            logger.info(f"Валидация {validated_model} прошла успешно")
            return validated_model
        
        except ValidationError as e:
            logger.error(f"Ошибка валидации: {e.json(indent=2)}")
            return None

    async def toJson(self, validated_object: BaseModel) -> dict[str, Any] | None:
        """
        Конвертирует Pydantic-модель в JSON-like словарь.

        validated_object: BaseModel - любая провалидированная модель
        """

        model_dict = validated_object.model_dump()
        logger.info(f"Конвертация в JSON-like формат прошла успешно")

        model_json = json.dumps(model_dict, indent=2)
        
        with open("photos.txt", 'w') as p:
            p.write(model_json)

        return model_json
    
    







