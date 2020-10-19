from tornado.web import Application, url
from views.index import IndexHandler, ParamHandler, SetRequestHeader, SetStatusCode, ErrorHandler, ReverseHandler, \
    SendJsonHandler, PathParams, FormParams, QueryParams, UpFileHandler, FinishHandler, CallOrderHandler
from config import settings


class MyApplication(Application):
    def __init__(self, *args, **kwargs):

        handlers = [url(r"/", IndexHandler, name="index handler"),
                    (r"/ph", ParamHandler, {"name": "徐红涛", "age": 22}),
                    (r"/srh", SetRequestHeader),
                    (r"/sr", SetStatusCode),
                    (r"/se", ErrorHandler),
                    url(r"/rh", ReverseHandler, {"name": "xuhongtao", "age": 23}, name="reverse handler"),
                    (r"/sj", SendJsonHandler),
                    (r"/pp/(?P<age>\w+)/(?P<name>\S+)", PathParams),
                    (r"/fp", FormParams),
                    (r"/qp", QueryParams),
                    (r"/uf", UpFileHandler),
                    (r'/fh', FinishHandler),
                    (r"/ch", CallOrderHandler),
                    ]
        super(MyApplication, self).__init__(handlers, **settings)