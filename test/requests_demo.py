#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/11 22:43'

import requests

r = requests.get('https://github.com/timeline.json')

print(r.text)

