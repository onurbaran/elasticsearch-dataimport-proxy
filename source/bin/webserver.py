from __future__ import print_function
from gevent.pywsgi import WSGIServer
from source.lib.endpoint import WebServer
from source.config.endpoint import endpoint_config

if __name__ == '__main__':
    print('Serving ')
    WSGIServer(('', endpoint_config['server_port']), WebServer.application).serve_forever()

