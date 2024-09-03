from ui_builder.domain.use_case import UseCase
from ui_builder.domain.value_objects.enums import TypeButton, TypeButtonSize


class CreateButtonUseCase(UseCase):

    def __init__(self,
                 text: str = '',
                 type_button: TypeButton = TypeButton.DEFAULT,
                 type_button_size: TypeButtonSize = TypeButtonSize.DEFAULT,
                 is_outline: bool = False):
        self.text = text
        self.type_button = type_button
        self.type_button_size = type_button_size
        self.is_outline = is_outline

    def execute(self):
        outline = ''

        if self.is_outline:
            outline = 'btn-outline'

        return f"""
        <button class="btn {outline} {self.type_button.value} {self.type_button_size.value}">{self.text}</button>
        """