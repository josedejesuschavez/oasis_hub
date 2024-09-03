from ui_builder.domain.use_case import UseCase
from ui_builder.domain.value_objects.enums import TypeTextInput, TypeInputColor, TypeInputSize, TypeInputIconPosition


class CreateTextInputWithTextLabelUseCase(UseCase):

    def __init__(self,
                 title: str = '',
                 value: str = '',
                 placeholder: str = '',
                 type_input_text: str = TypeTextInput.TEXT.value,
                 type_input_color: str = TypeInputColor.DEFAULT.value,
                 type_input_size: str = TypeInputSize.DEFAULT.value,
                 is_disabled: bool = False,
                 icon_position: str = TypeInputIconPosition.NONE.value):
        self.title = title
        self.value = value
        self.placeholder = placeholder
        self.type_input_text = type_input_text
        self.type_input_color = type_input_color
        self.type_input_size = type_input_size
        self.is_disabled = is_disabled
        self.icon_position = icon_position

    def execute(self) -> str:
        disabled = ''

        if self.is_disabled:
            disabled = 'disabled'

        return f"""
        <div class="form-control">
            <label class="input input-bordered flex items-center gap-2 {self.type_input_color} {self.type_input_size}">
            {self.title}
            <input
                type="{self.type_input_text}"
                class="grow"
                placeholder="{self.placeholder}"
                value="{self.value}"
                {disabled}
                />
            </label>
        </div>
        """
