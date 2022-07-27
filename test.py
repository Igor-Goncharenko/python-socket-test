import threading
import time


def print1():
    print("print1")


def input1():
    time.sleep(1)
    input("input1")


def print2():
    time.sleep(2)
    print("print2")


thr1 = threading.Thread(target=print1)
thr2 = threading.Thread(target=input1)
thr3 = threading.Thread(target=print2)

thr1.start()
thr2.start()
thr3.start()
