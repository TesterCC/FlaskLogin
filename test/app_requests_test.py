#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/11 23:02'

import requests

headers = {"User-Agent": "Mozilla/7.0 (Macintosh; Intel Mac OS X 11_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"}

r = requests.get('http://127.0.0.1:5000/index', headers=headers)

print(r.text)