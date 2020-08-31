from routes import routes
from controllers import PageNotFound


class App:
    def __init__(self, routes):
        self.routes = routes
        self._route_validate()

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        path = App._path_clear(path)
        view = PageNotFound()

        if path in self.routes:
            view = self.routes.get(path)

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return body

    def _route_validate(self):
        for item in self.routes:
            if not item.endswith('/'):
                raise ValueError("ERROR: addresses in the 'routes' file must end with'/'")
        return True

    @staticmethod
    def _path_clear(path):
        if path != '/':
            return path.split('/')[-1] + '/'
        return path


app = App(routes)
