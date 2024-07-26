from fastapi import APIRouter

from iam.infrastructure.ui.controllers import login_controller

router = APIRouter()

router.include_router(login_controller.router, prefix="/login")
