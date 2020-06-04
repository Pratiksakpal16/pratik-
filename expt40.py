from threading import *
import time
class a(Thread):
    def run(self):
        for i in range(10):
            print("live")
            time.sleep(2)
class b(Thread):
    def run(self):
        for i in range(10):
            print("wire")
            time.sleep(2)
obj1=a()
obj2=b()
obj1.start()
obj2.start()
