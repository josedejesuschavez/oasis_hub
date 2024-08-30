from ui_builder.domain.value_objects.enums import TypeInputText


class CreateTextInputUseCase:
    def __init__(self):
        pass

    def execute(
        self,
        value: str = "",
        placeholder: str = "",
        type_input_text: str = TypeInputText.TEXT.value,
    ):
        return f"""
        <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input
  type="{type_input_text}"
  class="form-control"
  id="exampleFormControlInput1" placeholder="{placeholder}" value="{value}" />
</div>
        """
