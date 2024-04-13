class fruit():
    def __init__ (self,col):
        self.color=col
    def display (self):
        print(self.color)
apple=fruit("red")

apple.display()