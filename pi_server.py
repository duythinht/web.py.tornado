from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from bootstrap import application

httpd = HTTPServer(WSGIContainer(application))
httpd.listen(8000)
IOLoop.instance().start()
