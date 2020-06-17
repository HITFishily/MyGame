# -*-coding:utf-8-*-
from threading import Timer
import time

def xx():
    print("xx")

def print_name(str, cb):
    print("i'm %s"%str)
    xx()
t = Timer(5,print_name,("superman",xx))
t.start()