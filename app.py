#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# http://www.mingjiao.org:8088/

from flask import Flask
import socket

node = Flask(__name__)


# 静态路由,最简单页面
@node.route('/', methods=['GET'])
def index():
    return f"This is {socket.gethostname()}, My IP is {socket.gethostbyname(socket.gethostname())}"


if __name__ == "__main__":
    node.run(host='0.0.0.0')


