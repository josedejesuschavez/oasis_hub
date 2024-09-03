from typing import List

from ui_builder.domain.use_case import UseCase


class CreateFormUseCase(UseCase):

    def __init__(self, rows: List[str]):
        self.rows = rows

    def execute(self) -> str:
        content = ''

        for row in self.rows:
            content = content + row

        return f"""
        <form>
        {content}
        </form>
        """