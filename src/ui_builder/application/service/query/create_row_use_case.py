from typing import List

from ui_builder.domain.use_case import UseCase


class CreateRowUseCase(UseCase):
    def __init__(self, cols: int, columns: List[UseCase]):
        self.cols = cols
        self.columns = columns

    def execute(self) -> str:
        content = ''

        for row in self.columns:
            content = content + row.execute()

        return f"""
        <div class="grid grid-cols-{self.cols} gap-4 p-2">
        {content}
        </div>
        """
