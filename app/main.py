from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.recommendation import router
from app.core.config import settings
from app.core.milvus_connection import connect_milvus


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🔹 startup
    connect_milvus()
    yield
    # 🔹 shutdown (optional)
    print("🛑 App shutdown")


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.include_router(router, prefix="")


@app.get("/health")
def health():
    return {"status": "ok"}