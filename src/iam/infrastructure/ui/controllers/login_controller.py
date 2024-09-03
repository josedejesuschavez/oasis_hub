from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from iam.infrastructure.ui.settings import env
from ui_builder.application.service.query.create_button_use_case import CreateButtonUseCase
from ui_builder.application.service.query.create_container_use_case import CreateContainerUseCase
from ui_builder.application.service.query.create_div_empty_use_case import CreateDivEmptyUseCase
from ui_builder.application.service.query.create_form_use_case import CreateFormUseCase
from ui_builder.application.service.query.create_row_use_case import CreateRowUseCase
from ui_builder.application.service.query.create_text_input_use_case import TextInput
from ui_builder.application.service.query.create_text_input.create_text_input_simple_use_case import CreateTextInputSimpleUseCase
from ui_builder.application.service.query.create_text_input_use_case import CreateTextInputUseCase
from ui_builder.application.service.query.create_text_input.create_text_input_with_icon_use_case import CreateTextInputWithIconUseCase
from ui_builder.application.service.query.create_text_input.create_text_input_with_text_label_use_case import CreateTextInputWithTextLabelUseCase
from ui_builder.domain.value_objects.enums import TypeInputSize, TypeInputColor, TypeButton

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
async def read_users(request: Request):
    row_1 = CreateRowUseCase(
        cols=2,
        columns=[
            CreateTextInputUseCase(text_input_type=TextInput.SIMPLE.value),
            CreateTextInputSimpleUseCase(type_input_color='input-info', placeholder='Ingresa tu nombre', title='Ingresa tu nombre')
        ])

    row_2 = CreateRowUseCase(
        cols=4,
        columns=[
            CreateDivEmptyUseCase(),
            CreateButtonUseCase(text='Hola mundo'),
            CreateDivEmptyUseCase(),
            CreateButtonUseCase(text='Hola mundo', type_button=TypeButton.PRIMARY),
        ])

    form = CreateFormUseCase(rows=[row_1, row_2])
    container = CreateContainerUseCase(content=form.execute())
    content_html = container.execute()

    #content_html = ''
    template = env.get_template('login.html')
    return template.render(
        request=request,
        content_html=content_html,
    )
