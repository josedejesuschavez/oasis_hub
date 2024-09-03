from ui_builder.domain.use_case import UseCase


class GetFormByIdUseCase(UseCase):
    def __init__(self, id: str):
        self.id = id

    def execute(self):
        return []