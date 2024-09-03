from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
#from ui_builder.application.service.query.create_text_input_simple_use_case import (
#    CreateTextInputSimpleUseCase,
#)
#from ui_builder.domain.value_objects.enums import TypeTextInput
from ui_builder.infrastructure.ui.settings import env

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    #create_text_input_use_case = CreateTextInputSimpleUseCase(type_input_text=TypeTextInput.PASSWORD.value)
    #input_str = create_text_input_use_case.execute()

    input_str = ''
    template = env.get_template("sample_book.html")
    return template.render(
        request=request,
        context={
            "input": input_str,
        },
    )
