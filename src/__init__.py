from fastapi import FastAPI

from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router

version = "v1"
version_prefix = f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description="A simple FastAPI application to manage books reviews with CRUD operations.",
    version=version_prefix,
)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
