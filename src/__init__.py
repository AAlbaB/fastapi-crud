from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"
version_prefix =f"/api/{version}"

app = FastAPI(
    title="Book Management API",
    description="A simple FastAPI application to manage books with CRUD operations.",
    version=version_prefix
)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["Books"])
