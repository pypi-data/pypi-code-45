class Submarine:

    def __init__(self,price=15000,budget=100000):
        self.captain = 'Prawit'
        self.sub_name = 'Uncle I'
        #self.price = 10000 #Million
        self.price = price #Million
        self.kilo = 0
        self.budget = budget 
        self.totalcost = 0

    def Missile(self):
        print('We are Department of Missile')

    def Calcommission(self):
        pc = 10
        percent = self.price * (pc/100)
        print('Loog! You got: {} Million Baht'.format(percent))

    def Goto(self,enemypoint,distance):
        print(f"Let's go to {enemypoint} Distance: {distance} KM")
        self.kilo = self.kilo + distance
        #self.kilo += distanc ยุบตัวแปรให้ใช้ตัวเดียว ด้วย +=
        self.Fuel()

    def Fuel(self):
        deisel = 20 # 20 bath / litre
        cal_feul_cost = self.kilo * deisel
        print('Current Feul Cost: {:,d} Baht'.format(cal_feul_cost)) # :,d เพื่อใส่ คอมมา บอกหลักพัน 
        self.totalcost += cal_feul_cost
    
    @property
    def BudgetRemaining(self):
        remaining = self.budget - self.totalcost
        print('Budget Remaining: {:,.2f} Baht'.format(remaining)) # :,.2f เพื่อให้เป็นค่า float
        return remaining

class ElectricSubmarine(Submarine):

    def __init__(self,price=15000,budget=400000):
        self.sub_name = 'Uncle III'
        self.battery_distance = 100000
        # Submarine can go out 100000 km / 100 percent
        super().__init__(price,budget)
    
    def Battery(self):
        allbattery = 100
        calculate = (self.kilo / self.battery_distance) * 100
        #print('CAL:',calculate)
        print('We have Battery Remaining: {} %'.format(allbattery-calculate))

    def Fuel(self):
        kilowattcost = 5 # 20 bath / litre
        cal_feul_cost = self.kilo * kilowattcost
        print('Current Power Cost: {:,d} Baht'.format(cal_feul_cost)) # :,d เพื่อใส่ คอมมา บอกหลักพัน 
        self.totalcost += cal_feul_cost


if __name__ == '__main__':
    tesla = ElectricSubmarine(40000,2000000)
    print(tesla.captain)
    print(tesla.budget)
    tesla.Goto('Japan',10000)
    print(tesla.BudgetRemaining)
    tesla.Battery()

    print('---------------------')

    kongtabbok = Submarine(40000,2000000)
    print(kongtabbok.captain)
    print(kongtabbok.budget)
    kongtabbok.Goto('Japan',10000)
    print(kongtabbok.BudgetRemaining)


'''
kongtabruew = Submarine(65400) #กองทัพเรือ
print("Captain " + kongtabruew.captain)
print(kongtabruew.sub_name)
print(kongtabruew.price)
print('------------------')
print(kongtabruew.kilo)
kongtabruew.Goto('China',7000)
print(kongtabruew.kilo)
kongtabruew.Fuel()
current_budget = kongtabruew.BudgetRemaining
print(current_budget * 0.2)
kongtabruew.Calcommission() 
##############################'''

# print("------ Submarine No 2 ----------")
# kongtabbok = Submarine(70000)
# print('Before...')
# print(kongtabbok.captain)
# print('After')
# kongtabbok.captain = 'Srivara'
# print(kongtabbok.captain)


# sub = ['Srivara','Uncle II',5000]
# print(sub[0])
# print(sub[1])
# print(sub[2])

