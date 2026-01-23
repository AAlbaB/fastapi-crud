from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from src.auth.dependencies import RoleChecker, get_current_user
from src.db.main import get_session
from src.db.models import User
from src.errors import ReviewNotFound

from .schemas import ReviewModel, ReviewCreateModel
from .service import ReviewService

review_service = ReviewService()
review_router = APIRouter()
admin_role_checker = Depends(RoleChecker(["admin"]))
user_role_checker = Depends(RoleChecker(["user", "admin"]))


@review_router.get(
    "/", response_model=list[ReviewModel], dependencies=[admin_role_checker]
)
async def get_all_reviews(
    session: AsyncSession = Depends(get_session),
) -> list[ReviewModel]:
    books = await review_service.get_all_reviews(session)

    return books


@review_router.get(
    "/{review_uid}", response_model=ReviewCreateModel, dependencies=[user_role_checker]
)
async def get_review(
    review_uid: UUID, session: AsyncSession = Depends(get_session)
) -> ReviewCreateModel:
    review = await review_service.get_review(review_uid, session)

    if not review:
        raise ReviewNotFound()

    return review


@review_router.post(
    "/book/{book_uid}",
    response_model=ReviewCreateModel,
    dependencies=[user_role_checker],
)
async def add_review_to_books(
    book_uid: UUID,
    review_data: ReviewCreateModel,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> ReviewCreateModel:
    new_review = await review_service.add_review_to_book(
        user_email=current_user.email,
        review_data=review_data,
        book_uid=book_uid,
        session=session,
    )

    return new_review


@review_router.delete(
    "/{review_uid}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[user_role_checker],
)
async def delete_review(
    review_uid: UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> None:
    await review_service.delete_review_to_from_book(
        review_uid=review_uid, user_email=current_user.email, session=session
    )

    return None
