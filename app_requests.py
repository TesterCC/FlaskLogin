#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/11 23:00'


from flask import Flask, request

app = Flask(__name__)


@app.route('/index')
def index():
    print(request.headers)
    return 'Hello RESTful!'


if __name__ == '__main__':
    app.run(debug=True)

