from jinja2 import Template


def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)
