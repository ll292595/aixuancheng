#!/usr/bin/env python
#
# aixuancheng
# 20160628
# Tornado: "HelloWorld"
#

from tornado import ioloop
from tornado import web

class index(web.RequestHandler):
    def get(self):
        self.render("index.html", title="Bettlekids")

class rebots(web.RequestHandler):
    def get(self):
        self.render("rebots.txt")

def app():
    return web.Application([
        (r"/", index),
        (r"/rebots.txt", rebots),
    ])

if __name__ == '__main__':
    Create_app = app()
    Create_app.listen(80)
    ioloop.IOLoop.current().start()

