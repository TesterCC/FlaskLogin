#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/11 22:49'


from io import BytesIO

import requests
from PIL import Image

r = requests.get('http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png')
i = Image.open(BytesIO(r.content))    # returns an instance of bytes while StringIO is an in-memory stream for text only. Use BytesIO instead.

# open pic
i.show()
