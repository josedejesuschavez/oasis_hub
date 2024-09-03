from ui_builder.domain.use_case import UseCase
from ui_builder.domain.value_objects.enums import TypeTextInput, TypeInputColor, TypeInputSize, TypeInputIconPosition


class CreateTextInputWithIconUseCase(UseCase):

    def __init__(self,
                 value: str = '',
                 placeholder: str = '',
                 type_input_text: str = TypeTextInput.TEXT.value,
                 type_input_color: str = TypeInputColor.DEFAULT.value,
                 type_input_size: str = TypeInputSize.DEFAULT.value,
                 is_disabled: bool = False,
                 icon_position: str = TypeInputIconPosition.NONE.value):
        self.value = value
        self.placeholder = placeholder
        self.type_input_text = type_input_text
        self.type_input_color = type_input_color
        self.type_input_size = type_input_size
        self.is_disabled = is_disabled
        self.icon_position = icon_position

    def execute(self) -> str:
        disabled = ''
        icon_right = ''
        icon_left = ''
        icon = f"""
        <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 16 16"
                    fill="currentColor"
                    class="h-4 w-4 opacity-70">
                    <path
                    fill-rule="evenodd"
                    d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
                    clip-rule="evenodd" />
                </svg>
        """

        if self.is_disabled:
            disabled = 'disabled'

        if self.icon_position == TypeInputIconPosition.RIGHT.value:
            icon_right = icon

        if self.icon_position == TypeInputIconPosition.LEFT.value:
            icon_left = icon

        return f"""
        <div class="form-control">
            <label class="input input-bordered flex items-center gap-2 {self.type_input_color} {self.type_input_size}">
                {icon_left}
                <input
                    type="{self.type_input_text}"
                    class="grow"
                    placeholder="{self.placeholder}"
                    value="{self.value}"
                    {disabled} />
                {icon_right} 
            </label>
        </div>
        """
