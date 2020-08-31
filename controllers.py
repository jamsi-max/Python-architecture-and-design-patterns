from render import render


class Index:
    def __call__(self):
        content = {
            'title': 'Index',
        }
        return '200 OK', [render('templates/index.html', context=content).encode('utf-8')]


class About:
    def __call__(self):
        content = {
            'address': 'Moscow, Leninsky, 12-4-123',
            'tel': '(000) 000-00-00'
        }
        return '200 OK', [render('templates/about.html', context=content).encode('utf-8')]


class PageNotFound:
    def __call__(self):
        content = {
            'title': '404 PAGE Not Found',
        }
        return '404 WHAT', [render('templates/notfound404.html', context=content).encode('utf-8')]
