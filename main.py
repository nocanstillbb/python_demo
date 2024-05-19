from log import Logger

l = Logger()

try:
    l.info("触发一个/0异常")
    zero = 0
    r = 10/zero
    l.info("手动抛出一个异常")
    raise Exception("thorw a exception")
except  Exception as e:
    l.critical(e)