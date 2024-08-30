from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from ui_builder.application.service.query.create_text_input_use_case import (
    CreateTextInputUseCase,
)
from ui_builder.domain.value_objects.enums import TypeInputText
from ui_builder.infrastructure.ui.settings import env

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    create_text_input_use_case = CreateTextInputUseCase()
    input_str = create_text_input_use_case.execute(
        type_input_text=TypeInputText.PASSWORD.value
    )

    template = env.get_template("sample_book.html")
    return template.render(
        request=request,
        context={
            "input": input_str,
        },
    )
