from pydantic import (
    BaseModel,
    ConfigDict
    )

class PhotoModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int