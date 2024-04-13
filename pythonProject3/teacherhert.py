class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display (self):
        print(self.name)
        print(self.regno)
t1=teacher("sam","01")
t2=teacher("ram","02")

t1.display()
t2.display()