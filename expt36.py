class bollywood:
    def actor(self):
        print("this is actor class")
    def singer(self):
        print("this is singer function")
class entertainment(bollywood):
    def dance(self):
        print("this is dance")
    def actor(self):
        super().actor()
        print("this is actors")
e=entertainment()
e.dance()
e.actor()
e.singer()
