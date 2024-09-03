from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from iam.infrastructure.ui.settings import env
from ui_builder.application.service.query.create_container_use_case import CreateContainerUseCase
from ui_builder.application.service.query.create_form_use_case import CreateFormUseCase
from ui_builder.application.service.query.create_row_use_case import CreateRowUseCase
from ui_builder.application.service.query.create_text_input_use_case import CreateTextInputUseCase
from ui_builder.application.service.query.create_text_input_simple_use_case import CreateTextInputSimpleUseCase
from ui_builder.application.service.query.create_text_input_use_case import CreateTextInputUseCase
from ui_builder.application.service.query.create_text_input_with_icon_use_case import CreateTextInputWithIconUseCase
from ui_builder.application.service.query.create_text_input_with_text_label_use_case import CreateTextInputWithTextLabelUseCase

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
async def read_users(request: Request):
    #input = CreateTextInputUseCase(text_input_type=TextInput.SIMPLE)
    #input.execute()
    #breakpoint()
    row_1 = CreateRowUseCase(
        cols=1,
        columns=[
            CreateTextInputSimpleUseCase(type_input_color='input-primary', type_input_size='').execute()
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
        cols=2,
        columns=[
            CreateTextInputSimpleUseCase(type_input_color='input-secondary', type_input_size='').execute(),
            CreateTextInputSimpleUseCase(type_input_color='input-secondary', type_input_size='').execute()
        ])
    row_1_content = row_1.execute()
    row_2_content = row_2.execute()
    row_3_content = row_3.execute()
    row_4_content = row_4.execute()
    form = CreateFormUseCase(rows=[row_1_content, row_2_content, row_3_content, row_4_content])
    container = CreateContainerUseCase(content=form.execute())
    content_html = container.execute()

    #content_html = ''
    template = env.get_template('login.html')
    return template.render(
        request=request,
        content_html=content_html,
    )
