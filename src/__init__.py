from fastapi import FastAPI

from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("servin has been stopped...")


version = "v1"
version_prefix = f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description="A simple FastAPI application to manage books reviews with CRUD operations.",
    version=version_prefix,
    lifespan=lifespan,
)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
