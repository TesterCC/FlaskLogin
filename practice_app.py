#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/12 00:21'


"""
3、实践：动手编写一个验证登录的程序
"""
import base64
import random
import time

from flask import Flask, request

app = Flask(__name__)

users = {
    "test": ["test13572468"]    # username  password
}

METHODS = ['GET', 'POST']    # for simplify setting


def gen_token(uid):
    a = ':'.join([str(uid), str(random.random()), str(time.time()+7200)])
    # print(type(a))  # type str
    a = a.encode()    # str to bytes
    # print(type(a))
    token = base64.b64encode(a)    # obj a ,a bytes-like object is required, not 'str'
    # print(token)

    # token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time()+7200)]))

    users[uid].append(token)      # add uid:token_value
    return token


def verify_token(token):
    _token = base64.b64decode(token)    # decryp token
    _token = _token.decode('utf-8')      # bytes to str

    # print(token)
    # print(users.get(_token.split(':')[0])[-1])

    if not users.get(_token.split(':')[0])[-1].decode('utf-8') == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():    # token is time out or not
        return 1   # token is valid
    else:
        return 0   # token is invalid


@app.route('/index', methods=['GET', 'POST'])     # 指定http method
def index():
    return 'Hello'


@app.route('/login', methods=['GET', 'POST'])
def login():
    tb = base64.b64decode(request.headers['Authorization'].split(' ')[-1])
    tb = tb.decode('utf-8')    # bytes to str
    # print(tb)   # 'test:test13572468'
    # print(tb.split(':'))

    # uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')

    uid, pw = tb.split(':')

    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'Login Failed.'


@app.route('/test', methods=METHODS)
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'Verified'
    else:
        return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
