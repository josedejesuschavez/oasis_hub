from ui_builder.domain.value_objects.enums import TypeInputText


class CreateTextInputUseCase:
    def __init__(self):
        pass

    def execute(self, value: str = '', placeholder: str = '', type_input_text: str = TypeInputText.TEXT.value):
        return f"""
        <input type="{type_input_text}" placeholder="{placeholder}" class="input w-full max-w-xs" value="{value}" />
        """