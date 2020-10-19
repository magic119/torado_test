import tornado.httpserver
import tornado.ioloop
from application import MyApplication


if __name__ == '__main__':
    app = MyApplication()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    tornado.ioloop.IOLoop.current().start()