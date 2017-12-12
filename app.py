#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/11 21:35'


from flask import Flask

app = Flask(__name__)


@app.route('/index/<user>')     # 带参数
def hello_world(user):
    return 'Hello %s' % user


if __name__ == '__main__':
    app.run(debug=True)
