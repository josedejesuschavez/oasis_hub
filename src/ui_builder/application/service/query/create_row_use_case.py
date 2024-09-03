from typing import List

from ui_builder.domain.use_case import UseCase


class CreateRowUseCase(UseCase):
    def __init__(self, cols: int, columns: List[str]):
        self.cols = cols
        self.columns = columns

    def execute(self) -> str:
        content = ''

        for row in self.columns:
            content = content + row

        return f"""
        <div class="grid grid-cols-{self.cols} gap-4">
        {content}
        </div>
        """
