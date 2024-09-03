from typing import List

from ui_builder.domain.use_case import UseCase


class CreateFormUseCase(UseCase):

    def __init__(self, rows: List[UseCase]):
        self.rows = rows

    def execute(self) -> str:
        content = ''

        for row in self.rows:
            content = content + row.execute()

        return f"""
        <form>
        {content}
        </form>
        """