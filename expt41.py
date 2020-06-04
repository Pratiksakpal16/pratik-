from threading import *
import time
class a(Thread):
    def run(self):
        a=int(input("Enter no."))
        b=int(input("Enter no."))
        c=a+b
        for i in range(10):
            print(c)
            time.sleep(2)
class b(Thread):
    def run(self):
        for i in range(1,10):
            print("Add")
            time.sleep(2)
obj1=a()
obj2=b()
obj1.start()
obj2.start()
