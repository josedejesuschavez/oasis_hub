from ui_builder.domain.use_case import UseCase


class CreateContainerUseCase(UseCase):

    def __init__(self, content: str):
        self.content = content

    def execute(self) -> str:
        return f"""
        <div class="container mx-auto p-4">
        {self.content}
        </div>
        """