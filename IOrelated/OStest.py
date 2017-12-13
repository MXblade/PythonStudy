#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

#获取系统名称
print( os.name )
#获取系统变量
print( os.environ )
print( os.environ.get('path'))

#查看当前目录的绝对路径
print( os.path.abspath('.'))
#在某个目录下创建新的目录，并将其展示，并未真的创建该目录
print( os.path.join('../files', 'testdir'))
#创建目录
#os.mkdir(os.path.join('../files', 'testdir'))
#删除目录
#os.rmdir(os.path.join('../files', 'testdir'))
#合并路径选用path.join可以处理不同系统的路径分隔符，若分离路径选择path.split
print( os.path.split(os.path.abspath('../files/write.txt')))
#分离扩展名，选用path.splitext
print( os.path.splitext(os.path.abspath('../files/write.txt')))

#rename文件名
#os.rename('write.txt', 'write2.txt')
#删除文件
#os.remove('write2.txt')



print('---------------------------------')
print('在当前目录及其子目录下的的文件名查找包含指定字段的文件，并打印绝对路径')
def findfile(filestr, path = os.path.abspath('.')):
    for x in os.listdir('.'):
        x_full = os.path.join(path, x)
        if os.path.isdir(x_full):
            findfile(filestr, x_full)
        elif os.path.isfile(x_full) and os.path.split(x_full)[1].__contains__(filestr):
            print( x_full )
        else:
            pass

if __name__ == '__main__':
    findfile('O')

