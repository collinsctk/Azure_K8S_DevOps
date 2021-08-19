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
#     return f"This is QYTAKS:{socket.gethostname()}, My IP is {socket.gethostbyname(socket.gethostname())}"
    return_str=f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>乾颐堂Azure测试</title>
        </head>
        <body>
        <img src="/static/qytanglogo.png"/>
        <h3>This is QYTAKS:{socket.gethostname()}, My IP is {socket.gethostbyname(socket.gethostname())}</h3>
        </body>
        </html>"""
    return return_str

@node.route('/forbidden', methods=['GET'])
def forbiden():
    return_str=f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>乾颐堂Azure测试</title>
        </head>
        <body>
        <img src="/static/qytanglogo.png"/>
        <h3>此页面应该被WAF禁止</h3>
        </body>
        </html>"""
    return return_str
    
if __name__ == "__main__":
    node.run(host='0.0.0.0', port=80)


