from ui_builder.domain.use_case import UseCase


class CreateDivEmptyUseCase(UseCase):

    def __init__(self):
        pass

    def execute(self):
        return """
        <div></div>
        """