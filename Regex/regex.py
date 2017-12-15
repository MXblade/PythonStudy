#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import re

s = re.match('^\d{3}\-\d{3,8}', '010-1231241')
print(s)

re_mail = re.compile(r'^([0-9a-zA-Z][0-9a-zA-Z\.]*)@([0-9a-z]*\.[a-z]+)$')


def is_valid_email(addr):
    if re_mail.match(addr):
        return True


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


re_name_mail = re.compile(r'(<([a-zA-Z\s]+)>)*[\s]*([a-zA-Z]+)@([a-zA-Z]+\.[a-zA-Z]+)$')


def name_of_email(addr):
    result = re_name_mail.match(addr)
    if result.group(1)==None:
        return result.group(3)
    else:
        return result.group(2)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')