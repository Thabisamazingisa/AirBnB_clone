"""review class inhereted from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes the Review class"""
        super().__init__(*args, **kwargs)
