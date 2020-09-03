import json
import chardet
import time
import urllib

from routes import routes
from controllers import PageNotFound


class App:
    def __init__(self, routes):
        self.routes = routes
        self._route_validate()

    def __call__(self, environ, start_response):

        App.post(environ) if environ.get('REQUEST_METHOD') == 'POST' else App.get(environ)

        path = environ.get('PATH_INFO', None)
        path = App._path_clear(path)

        view = PageNotFound()

        if path in self.routes:
            view = self.routes.get(path)

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return body

    @staticmethod
    def post(environ):
        length = int(environ.get('CONTENT_LENGTH', '0'))
        data = environ.get('wsgi.input').read(length)

        if length > 26:
            data_str = data.decode(chardet.detect(data)['encoding'])
            data_dict = App.parse_input(data_str.splitlines())
            App.write_json(data_dict)

    @staticmethod
    def get(environ):
        if environ.get('QUERY_STRING'):
            data = urllib.parse.unquote(environ.get('QUERY_STRING'))
            data_dict = App.parse_input(data.split('&'))
            App.write_json(data_dict)

    @staticmethod
    def parse_input(data: str) -> dict:
        """
        Function parse data str
        :param data: str
        :return: dict
        """
        result = {}
        for item in data:
            key, val = item.split('=')
            result[key] = val
        result['date'] = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        return result

    @staticmethod
    def write_json(message_dict: dict):
        """
        Function write json file from python dict
        :param message_dict: dict
        """
        try:
            data = json.load(open('data_base.json'))
        except:
            data = []

        if message_dict:
            data.append(message_dict)
            with open('data_base.json', 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def _path_clear(path: str):
        """
        The function checks/adds '/' at the end of the route for correct routing
        :param path: str
        :return: str
        """
        if path != '/':
            return path.split('/')[-1] + '/'
        return path

    def _route_validate(self):
        """
        The function checks for '/' at the end of the address
        :return:
        """
        for item in self.routes:
            if not item.endswith('/'):
                raise ValueError("ERROR: addresses in the 'routes' file must end with'/'")
        return True


app = App(routes)
