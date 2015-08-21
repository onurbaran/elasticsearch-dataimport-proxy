__author__ = 'onurbaran'
import gevent
from gevent import Greenlet
from gevent.queue import Queue
from source.config.es_importer import es_importer_config as config
from elasticsearch import Elasticsearch,helpers

# curl -s -XPOST localhost:9200/_bulk --data-binary @requests;

class Importer(gevent.Greenlet):

    def __init__(self):
        self.inbox = Queue()
        self._es = Elasticsearch({"host": config['es_host'], "port": config['es_port']})
        Greenlet.__init__(self)

    def _process(self, message):
        helpers.bulk(self._es, message)

    def _run(self):
        self.running = True

        while self.running:
            message = self.inbox.get()
            self._process(message)


