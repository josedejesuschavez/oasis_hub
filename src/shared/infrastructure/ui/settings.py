from jinja2 import FileSystemLoader

template_loader = FileSystemLoader(
    [
        "shared/infrastructure/ui/templates",
    ]
)
