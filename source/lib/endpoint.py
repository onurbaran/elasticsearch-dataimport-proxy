__author__ = 'onurbaran'
from source.actors.Base import Importer

class WebServer(object):

    @staticmethod
    def application(env, start_response):
        content_actor = Importer()
        content_actor.start()
        if env['PATH_INFO'] == '/new_content':
            start_response('200 OK', [('Content-Type', 'application/json')])
            content_actor.inbox.put("new_content")
            return [b'''ok''']
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'<h1>Not Found</h1>']