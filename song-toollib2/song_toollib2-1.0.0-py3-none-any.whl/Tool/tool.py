name = "li4"

def jump1():
    print("jump1")


class Person:
    def __init__(self,name):
        self.name = name

    def jump2(self):
        print("{0} on jump2".format(self.name))



if __name__ == "__main__" :
    p = Person("li4")
    p.play()
