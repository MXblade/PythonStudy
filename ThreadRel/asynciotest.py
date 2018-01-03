import threading
import asyncio

@asyncio.coroutine
def hello(x):
    print('Hello world!%s (%s)' % (x ,threading.currentThread()))
    yield  print('----')
    print('Hello again!%s (%s)' % (x, threading.currentThread()))

loop = asyncio.get_event_loop()
tasks = [hello(s) for s in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
asyncio.open_connection()