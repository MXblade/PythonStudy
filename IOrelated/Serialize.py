#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#序列化

import pickle

#pickle进行序列化，返回的是bytes
d = dict(name = 'Bob', age = 20, score = 98)
print(pickle.dumps(d))
picpath = r'../files/Serialize/pickle_dump.txt'
f = open(picpath, 'wb')
pickle.dump(d, f)
f.close()

f = open(picpath, 'rb')
print(pickle.load(f))
f.close()

import json

#json进行序列化，返回的是str
print(json.dumps(d))
jsonpath = r'../files/Serialize/json_dump.txt'
f = open(jsonpath, 'w')
json.dump(d, f)
f.close()

f = open(jsonpath, 'r')
print(json.load(f))
f.close()

#通过json对class进行序列化，需要先进行class2dict的转化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 28, 99)

def student2dict(std):
    return {'name' : std.name, 'age' : std.age, 'score' : std.score}

f = open(jsonpath, 'w')
json.dump(s, f, default=student2dict)
#一般class实例会有__dict__属性，也可使用该属性来进行转化
#json.dump(s, f, default=lambda obj:obj.__dict__)
f.close()

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

f = open(jsonpath, 'r')
print(json.load(f, object_hook=dict2student))
f.close()

