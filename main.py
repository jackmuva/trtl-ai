from fastapi import FastAPI
from routers import brainstorm

app = FastAPI()
app.include_router(brainstorm.router)
@app.get("/")
async def root():
    return "healthy"