from fastapi import FastAPI

from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router

from .errors import register_all_errors
from .middleware import register_middleware

version = "v1"
version_prefix = f"/api/{version}"

app = FastAPI(
    title="BookStack API",
    description="A FastAPI application for managing books, reviews and tags with CRUD operations.",
    version=version_prefix,
)

register_all_errors(app)
register_middleware(app)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"])
