#!/usr/bin/env python3
# -*- coding:utf-8 -*-

relapath = r'../files/write.txt'
abspath = r'c:\PycharmProjects\PythonStudy\files\write.txt'

#相对路径写入
f = open(relapath, 'w', encoding='utf-8')
f.write('test write relapath')
f.close()

#绝对路径写入
f = open(abspath, 'a', encoding='utf-8')
f.write('\ntest addwrite abspath')
f.write('test encoding 中文')
f.close()

#测试with写入
with open(relapath, 'a', encoding='utf-8', errors='ignore') as f:
    f.write('\ntest withwrite and errorsignore ')

#测试读取文件
f = open(relapath, 'r', encoding='utf-8')
print(f.read())
f.close()




