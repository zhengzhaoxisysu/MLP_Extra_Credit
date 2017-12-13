from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class ChartHandler(RequestHandler):
    def get(self):
        user = self.get_argument('user')
        self.write('Hello, ' + user)


if __name__ == "__main__":
    handler_mapping = [
                       (r'/', ChartHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
