from fastapi import APIRouter
from models.UrlObject import UrlObject

router = APIRouter()
@router.post("/brainstorm/")
async def create_item(urlObject: UrlObject):
    return urlObject