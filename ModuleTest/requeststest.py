#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

r = requests.get('http://www.douban.com/')
print(r.status_code)
#print(r.text)

r = requests.get('http://www.douban.com/search', params={'p':'python','cat':1001})
print(r.status_code)