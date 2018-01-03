def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('begin')
        yield b
        # print b
        # yield from range(10)
        # yield 'third'
        print('+++')
        a, b = b, a + b
        n = n + 1
f=fab3(5)
print("f是一个可迭代对象，并没有执行函数")
print(f)
print('fab3返回的是一个iterable 对象，可以用for循环获取值')
print(f.__next__())

print('-------')
print(f.__next__())
# for n in f:
#     print(n)
#     print('-------')