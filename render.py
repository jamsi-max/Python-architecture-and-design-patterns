from jinja2 import Template
import os


class DirectoryNotFound(Exception):
    pass


def render(template_name, **kwargs) -> str:
    """
    Рендер шаблона
    :param template_name: file_name
    :param kwargs: content
    :return: str
    """
    if os.path.exists('templates'):
        template_name_abs = os.path.join(os.path.abspath('templates'), template_name)

        with open(template_name_abs, encoding='utf-8') as file:
            template = Template(file.read())
        return template.render(**kwargs)

    else:
        raise DirectoryNotFound("There is no directory with 'templates'!")

