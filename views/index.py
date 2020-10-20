from tornado.web import RequestHandler
from config import UP_FILE_PATH


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class ParamHandler(RequestHandler):
    def initialize(self, name, age) -> None:
        self.name = name
        self.age = age

    def get(self, *args, **kwargs):
        self.write(self.name+str(self.age))


class SetRequestHeader(RequestHandler):
    def set_default_headers(self) -> None:
        self.set_header("version", "1.1")
        self.set_header("bug", "repaired")

    def get(self, *args, **kwargs):
        self.set_header("version", "1.2")
        self.write("setrequestheader")


class SetStatusCode(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(999, "not define")
        self.write("set_status")


class ErrorHandler(RequestHandler):
    def write_error(self, status_code: int, **kwargs) -> None:
        if status_code == 500:
            code = 500
        elif status_code == 404:
            code = 404
        else:
            code = 999
            reason = "unknown reason"
            self.set_status(code, reason)
        self.set_status(code)

        self.write("set_status之后的代码继续执行")

    def get(self, *args, **kwargs):

        error = self.get_query_argument("error")

        if error == "0":
            self.send_error(500)

            print("send_error之后代码继续执行")
        else:
            self.write("you are right")


class ReverseHandler(RequestHandler):
    def initialize(self, name, age) -> None:
        pass

    def get(self, *args, **kwargs):
        url = self.reverse_url(name="index handler")
        self.redirect(url, permanent=True)
        self.set_header("Content_type", "application/json")
        self.write("<a href = %s>去首页</a>" % url)


class SendJsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json;charset=utf-8")
        self.write({"name": "徐红涛"})


class PathParams(RequestHandler):
    def get(self, age, name, *args, **kwargs):

        print(name)
        print(age)

        self.write("接受数据成功")


class FormParams(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("form.html")

    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        like_list = self.get_body_arguments("like")
        print(username, password, like_list)

        self.write("接受数据成功")


class QueryParams(RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_query_argument("name", strip=True)
        age_list = self.get_query_arguments("age", strip=True)
        # print(name, age_list)

        self.write("接受数据成功")


class UpFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("file.html")


    def post(self, *args, **kwargs):
        file_dict = self.request.files

        for file in file_dict:
            data_list = file_dict[file]
            for data_dict in data_list:
                data_name = data_dict["filename"]
                data = data_dict["body"]
                with open(UP_FILE_PATH+r"\\"+data_name, "wb") as f:
                    f.write(data)

        self.write("接收数据成功")


class FinishHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.write("name: 徐红涛")
        self.write("age: 22")
        self.write("location: JiangSu Province")

        self.finish()


class CallOrderHandler(RequestHandler):
    def initialize(self, *args, **kwargs):
        print("initialize")

    def prepare(self, *args, **kwargs):
        print("prepare")

    def get(self, *args, **kwargs):
        self.write("调用执行顺序")
        print("get")
        self.send_error(500)

    def write_error(self, status_code, **kwargs) -> None:
        print("write error")

    def on_finish(self) -> None:
        print("on finish")

    def set_default_headers(self) -> None:
        print("set_header")

    def set_status(self, status_code: int, reason: str = None) -> None:
        print("set_status")

    def set_header(self, name: str, value) -> None:
        pass

    def add_header(self, name: str, value) -> None:
        pass