#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import chardet

#检测字符串编码格式

print(chardet.detect(b'hello test'))


data = '天长地久有时尽，此恨绵绵无绝期'.encode('utf-8')
print(data)
print(chardet.detect(data))