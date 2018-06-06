#! /usr/bin/env python3
# -*-coding:utf-8 -*-

import chardet

def typechange(filename, targetfilename,datatype):

    file = open(filename, "rb")#要有"rb"，如果没有这个的话，默认使用gbk读文件。
    buf = file.read()
    result = chardet.detect(buf)
    file = open(filename,"r",encoding=result["encoding"])
    content = file.readlines()
    file = open('../files/testtxt/datatype_target.txt', 'w', encoding=datatype)


assert typechange('../files/testtxt/datatype_origin.txt', '../files/testtxt/datatype_target.txt', 'utf-8')
