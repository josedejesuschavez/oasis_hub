from enum import Enum

from ui_builder.application.service.query.create_text_input_simple_use_case import CreateTextInputSimpleUseCase
from ui_builder.application.service.query.create_text_input_with_icon_use_case import CreateTextInputWithIconUseCase
from ui_builder.application.service.query.create_text_input_with_text_label_use_case import \
    CreateTextInputWithTextLabelUseCase
from ui_builder.domain.use_case import UseCase


class TextInput(Enum):
    SIMPLE = CreateTextInputSimpleUseCase
    WITH_ICON = CreateTextInputWithIconUseCase
    WITH_TEXT_LABEL = CreateTextInputWithTextLabelUseCase


class CreateTextInputUseCase(UseCase):

    def __init__(self, text_input_type):
        self.text_input_type = text_input_type

    def execute(self) -> str:

        return """
        """
