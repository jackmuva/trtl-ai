from pydantic import BaseModel

class UrlObject(BaseModel):
    url: str