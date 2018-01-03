#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'root',  database = 'test')
cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# print(cursor.rowcount)
# conn.commit()
#cursor.close()

cursor.execute('select * from user ')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
