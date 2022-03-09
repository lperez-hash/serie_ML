from pydantic import BaseModel
from pydantic import Field

class Prediction_response(BaseModel):
    prediction:list = Field(..., description='Vector de P puntos predichos por el modelo')

    class Config:
        schema_extra={
            'example': {
                'prediction': [123.3, 456.2, 452.7]
            }
        }