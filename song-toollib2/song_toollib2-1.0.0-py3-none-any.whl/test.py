name = zhang3

def play1():
    print("play1")


class Person:
    def __init__(self,name):
        self.name = name

    def play2(self):
        print("{0} on play".format(self.name))



if __name__ == "__main__" :
    p = Person("zhang3")
    p.play()