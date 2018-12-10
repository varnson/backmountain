from gevent.pywsgi import WSGIServer,WSGIHandler
from flask import request, Flask
from router import rules

class RestServer(object):
    def __init__(self, *args, **kwargs):
        self.application=Flask(__name__)
        for rule in rules:
            self.application.add_url_rule(**rule)
        

    def startServer(self, port):
        
        self.server = WSGIServer(('127.0.0.1', port),self.application)
        self.server.serve_forever()


    def stop(self, *args, **kwargs):
        super.stop(self, *args, **kwargs)


if __name__ == '__main__':
    server = RestServer()
    server.startServer(9000)

