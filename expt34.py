class cal:
    def __init__(self):
        self.a=int(input("enter first no."))
        self.b=int(input("enter second no."))
    def add(self):
        self.c=self.a+self.b
        print(self.c)
    def sub(self):
        self.c=self.a-self.b
        print(self.c)
e=cal()
e.add()
e.sub()
