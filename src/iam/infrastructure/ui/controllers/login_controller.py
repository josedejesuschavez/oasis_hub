from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from iam.infrastructure.ui.settings import env
from ui_builder.application.service.query.create_container_use_case import CreateContainerUseCase
from ui_builder.application.service.query.create_form_use_case import CreateFormUseCase
from ui_builder.application.service.query.create_row_use_case import CreateRowUseCase
from ui_builder.application.service.query.create_text_input_use_case import TextInput
from ui_builder.application.service.query.create_text_input.create_text_input_simple_use_case import CreateTextInputSimpleUseCase
from ui_builder.application.service.query.create_text_input_use_case import CreateTextInputUseCase
from ui_builder.application.service.query.create_text_input.create_text_input_with_icon_use_case import CreateTextInputWithIconUseCase
from ui_builder.application.service.query.create_text_input.create_text_input_with_text_label_use_case import CreateTextInputWithTextLabelUseCase
from ui_builder.domain.value_objects.enums import TypeInputSize, TypeInputColor

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
async def read_users(request: Request):
    row_1 = CreateRowUseCase(
        cols=2,
        columns=[
            CreateTextInputUseCase(text_input_type=TextInput.SIMPLE.value).execute(),
            CreateTextInputSimpleUseCase(type_input_color='input-info', placeholder='Ingresa tu nombre', title='Ingresa tu nombre').execute()
        ])
    row_2 = CreateRowUseCase(
        cols=1,
        columns=[
            CreateTextInputWithIconUseCase(placeholder='Password', type_input_color='input-primary', icon_position='left').execute()
        ])
    row_3 = CreateRowUseCase(
        cols=1,
        columns=[
            CreateTextInputWithTextLabelUseCase(title='Email', type_input_text='password', placeholder='Password', type_input_color='input-primary',
                                           icon_position='left').execute()
        ])

    row_4 = CreateRowUseCase(
        cols=4,
        columns=[
            CreateTextInputSimpleUseCase(type_input_size=TypeInputSize.SM.value, type_input_color='input-secondary').execute(),
            CreateTextInputSimpleUseCase(type_input_color=TypeInputColor.INFO.value).execute(),
            CreateTextInputSimpleUseCase(type_input_color=TypeInputColor.INFO.value).execute(),
            CreateTextInputSimpleUseCase(type_input_color=TypeInputColor.INFO.value).execute()
        ])

    row_5 = CreateRowUseCase(
        cols=1,
        columns=[
            CreateTextInputSimpleUseCase(type_input_color='input-info', type_input_size='', placeholder='Hola mundo',
                                         title='Hello world').execute()
        ])
    row_1_content = row_1.execute()
    row_2_content = row_2.execute()
    row_3_content = row_3.execute()
    row_4_content = row_4.execute()
    row_5_content = row_5.execute()
    form = CreateFormUseCase(rows=[row_1_content, row_2_content, row_3_content, row_4_content, row_5_content])
    container = CreateContainerUseCase(content=form.execute())
    content_html = container.execute()

    #content_html = ''
    template = env.get_template('login.html')
    return template.render(
        request=request,
        content_html=content_html,
    )
