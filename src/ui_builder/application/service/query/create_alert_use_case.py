from ui_builder.domain.value_objects.enums import TypeAlert


class CreateAlertUseCase:
    def __init__(self):
        pass

    def execute(self, message: str, icon: str, type_alert: str = TypeAlert.ALERT.value, stroke: str = 'stroke-info', is_closeable: bool = False):
        button_close_alert = ""
        htmx_attributes = ""
        if is_closeable:
            button_close_alert = f"""<button @click="show = false" class="close-btn">&times;</button>"""
            htmx_attributes = f"""x-data="{{ show: true }}" x-show="show" """

        return f"""
        <div role="alert" class="{type_alert}" {htmx_attributes}>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="{stroke} shrink-0 w-6 h-6">{icon}</svg>
            <span>{message}</span>
            {button_close_alert}
        </div>"""
