from fastapi import APIRouter

from ui_builder.infrastructure.ui.controllers import sample_book_controller

router = APIRouter()

router.include_router(
    sample_book_controller.router, prefix="/sample_book", tags=["ui_builder"]
)
