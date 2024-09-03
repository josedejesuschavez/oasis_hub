from ui_builder.domain.use_case import UseCase
from ui_builder.domain.value_objects.enums import TypeTextInput, TypeInputColor, TypeInputSize


class CreateTextInputSimpleUseCase(UseCase):

    def __init__(self,
                 title: str = '',
                 value: str = '',
                 placeholder: str = '',
                 type_input_text: str = TypeTextInput.TEXT.value,
                 type_input_color: str = TypeInputColor.DEFAULT.value,
                 type_input_size: str = TypeInputSize.DEFAULT.value,
                 is_disabled: bool = False):
        self.title = title
        self.value = value
        self.placeholder = placeholder
        self.type_input_text = type_input_text
        self.type_input_color = type_input_color
        self.type_input_size = type_input_size
        self.is_disabled = is_disabled

    def execute(self):
        title = ''
        disabled = ''

        if self.title != '':
            title = f"""
            <label class="label">
                <span class="label-text">{self.title}</span>
            </label>
            """

        if self.is_disabled:
            disabled = 'disabled'

        return f"""
        <div class="form-control">
            {title}
            <input
                type="{self.type_input_text}"
                placeholder="{self.placeholder}"
                value="{self.value}"
                {disabled}
                class="input input-bordered {self.type_input_color} {self.type_input_size}">
        </div>
        """
