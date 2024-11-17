from fastapi import APIRouter
from models.UrlObject import UrlObject
from services.LlmPrompt import promptLlm
from services.crawler import crawlSite

router = APIRouter()
@router.post("/brainstorm/")
async def brainstorm(urlObject: UrlObject):
    texts = crawlSite(urlObject.url)
    return promptLlm(texts)