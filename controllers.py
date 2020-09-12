from render import render


def get_style(file_css):
    """
    Function helps you connect styles to html
    """
    with open(file_css, encoding='utf-8') as file:
        return file.read()


class Index:
    def __call__(self):
        content = {
            'title': 'Framework',
            'style': get_style('templates/style/style.css')
        }
        return '200 OK', [render('index.html', context=content).encode('utf-8')]


class About:
    def __call__(self):
        content = {
            'title': 'About',
            'address': 'Moscow, Leninsky, 12-4-123',
            'tel': '(000) 000-00-00',
            'style': get_style('templates/style/style.css')
        }
        return '200 OK', [render('about.html', context=content).encode('utf-8')]


class Contacts:
    def __call__(self):
        content = {
            'title': 'Feedback',
            'style': get_style('templates/style/style.css')
        }
        return '200 OK', [render('contacts.html', context=content).encode('utf-8')]


class PageNotFound:
    def __call__(self):
        content = {
            'title': '404 PAGE Not Found',
        }
        return '404 WHAT', [render('notfound404.html', context=content).encode('utf-8')]
