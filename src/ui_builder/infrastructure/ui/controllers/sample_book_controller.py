from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from ui_builder.application.service.query.create_text_input_use_case import CreateTextInputUseCase
from ui_builder.domain.value_objects.enums import TypeInputText


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    create_text_input_use_case = CreateTextInputUseCase()
    input = create_text_input_use_case.execute(type_input_text=TypeInputText.PASSWORD.value)
    return templates.TemplateResponse(
        request=request,
        name="ui_builder/sample_book.html",
        context={
            'input': input,
        }
    )
