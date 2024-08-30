from jinja2 import Environment
from shared.infrastructure.ui.settings import template_loader


template_loader.searchpath.append("ui_builder/infrastructure/ui/templates")
env = Environment(loader=template_loader)
