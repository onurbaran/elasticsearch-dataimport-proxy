__author__ = 'onurbaran'

from source.config.endpoint import endpoint_config

class WebServer(object):

    @staticmethod
    def application(env, start_response):

        if env['PATH_INFO'] == '/new_content':
            start_response('200 OK', [('Content-Type', 'application/json')])
            return [b'''ok''']
            return [b'''ok''']
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'<h1>Not Found</h1>']