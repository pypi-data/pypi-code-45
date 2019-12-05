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

