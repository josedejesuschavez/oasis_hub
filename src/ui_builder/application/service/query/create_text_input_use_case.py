from abc import ABCMeta
from enum import Enum

from ui_builder.application.service.query.create_text_input.create_text_input_simple_use_case import CreateTextInputSimpleUseCase
from ui_builder.application.service.query.create_text_input.create_text_input_with_icon_use_case import CreateTextInputWithIconUseCase
from ui_builder.application.service.query.create_text_input.create_text_input_with_text_label_use_case import \
    CreateTextInputWithTextLabelUseCase
from ui_builder.domain.use_case import UseCase
from ui_builder.domain.value_objects.enums import TypeTextInput, TypeInputColor, TypeInputSize, TypeInputIconPosition


class TextInput(Enum):
    SIMPLE = CreateTextInputSimpleUseCase
    WITH_ICON = CreateTextInputWithIconUseCase
    WITH_TEXT_LABEL = CreateTextInputWithTextLabelUseCase


class CreateTextInputUseCase(UseCase):

    def __init__(self,
                 text_input_type: ABCMeta = TextInput.SIMPLE.value,
                 title: str = '',
                 value: str = '',
                 placeholder: str = '',
                 type_input_text: str = TypeTextInput.TEXT.value,
                 type_input_color: str = TypeInputColor.DEFAULT.value,
                 type_input_size: str = TypeInputSize.DEFAULT.value,
                 is_disabled: bool = False,
                 icon_position: str = TypeInputIconPosition.NONE.value
                 ):
        self.title = title
        self.value = value
        self.placeholder = placeholder
        self.type_input_text = type_input_text
        self.type_input_color = type_input_color
        self.type_input_size = type_input_size
        self.is_disabled = is_disabled
        self.icon_position = icon_position

        if issubclass(text_input_type, CreateTextInputSimpleUseCase):
            self.text_input_type = CreateTextInputSimpleUseCase(
                title=self.title,
                value=self.value,
                placeholder=self.placeholder,
                type_input_text=self.type_input_text,
                type_input_color=self.type_input_color,
                type_input_size=self.type_input_size,
                is_disabled=self.is_disabled,
            )

        if issubclass(text_input_type, CreateTextInputWithIconUseCase):
            self.text_input_type = CreateTextInputWithIconUseCase(
                value=self.value,
                placeholder=self.placeholder,
                type_input_text=self.type_input_text,
                type_input_color=self.type_input_color,
                type_input_size=self.type_input_size,
                is_disabled=self.is_disabled,
                icon_position=self.icon_position,
            )

        if issubclass(text_input_type, CreateTextInputWithTextLabelUseCase):
            self.text_input_type = CreateTextInputWithTextLabelUseCase(
                title=self.title,
                value=self.value,
                placeholder=self.placeholder,
                type_input_text=self.type_input_text,
                type_input_color=self.type_input_color,
                type_input_size=self.type_input_size,
                is_disabled=self.is_disabled,
                icon_position=self.icon_position,
            )

    def execute(self) -> str:
        return self.text_input_type.execute()
