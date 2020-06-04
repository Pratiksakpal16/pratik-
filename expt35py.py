class cal:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def add(self):
        self.c=self.a+self.b
        print(self.c)
e=cal(10,20)
e.add()
