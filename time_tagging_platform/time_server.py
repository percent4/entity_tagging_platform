# -*- coding: utf-8 -*-
# time: 2019-08-08
# place: Xinbeiqiao, Beijing

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from utils import get_max_num

#定义端口为9005
define("port", default=9005, help="run on the given port", type=int)

# GET请求
class QueryHandler(tornado.web.RequestHandler):
    # get函数
    def get(self):
        self.render('time_index.html', data = ['', []])

# POST请求
class PostHandler(tornado.web.RequestHandler):
    # post函数
    def post(self):

        # 获取前端参数, event, time, index
        event = self.get_argument('event')
        times = self.get_arguments('time')
        indices = self.get_arguments('index')
        print(event)
        print(times)
        print(indices)

        # 前端显示序列标注信息
        tags = ['O'] * len(event)

        for time, index in zip(times, indices):
            index = int(index)
            tags[index] = 'B-TIME'
            for i in range(1, len(time)):
                tags[index+i] = 'I-TIME'

        data = [event, tags]

        self.render('time_index.html', data=data)

        # 保存为txt文件
        dir_path = './time_output'
        with open('./%s/%s.txt' % (dir_path, get_max_num(dir_path)+1), 'w', encoding='utf-8') as f:
            for char, tag in zip(event, tags):
                f.write(char+'\t'+tag+'\n')


# 主函数
def main():
    # 开启tornado服务
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[(r'/query', QueryHandler),
                      (r'/result', PostHandler)
                      ], #网页路径控制
            template_path=os.path.join(os.path.dirname(__file__), "templates") # 模板路径
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

main()