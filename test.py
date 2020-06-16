# -*-coding:utf-8-*-
from threading import Timer
import time
def print_name(str):
    print("i'm %s"%str)
t = Timer(5,print_name,("superman",))
t.start()
time.sleep(3)
t.cancel()