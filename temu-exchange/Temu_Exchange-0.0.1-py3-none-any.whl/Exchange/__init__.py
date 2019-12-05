class Convert:
    def __init__(self,u,w):
        self.unit = u
        self.weight = w

    def changing(self):       
        if self.unit.upper() == "L":
            converted = self.weight * 0.45
            print(f"You are {converted} kg")
        else:
            converted = self.weight / 0.45
            print(f"You are {converted} pounds")

unit = input("(L)bs or (K)g: ")
weight = int(input("weight: "))
c = Convert(unit,weight)
c.changing()