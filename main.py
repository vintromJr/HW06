class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand, capacity, tank_volume, consumption):
        self.brand = brand  #Марка автомобіля
        self.passengers = []  #Перелік пасажирів
        self.capacity = capacity  #Вмістимість салону авто
        self.tank_volume = tank_volume  #Об'єм бензобака
        self.fuel = 0  #Кількість пального
        self.consumption = consumption  #Витрата пального в літрах на 100 км

    def add_fuel(self, fuel):
        if self.fuel + fuel <= self.tank_volume: self.fuel += fuel
        else: self.fuel = self.tank_volume

    def add_passenger(self, *args):
        temp = []
        for i in args:
            if len(self.passengers) < self.capacity: self.passengers.append(i)
            else: temp.append(i.name)
        if len(temp) > 0:
            print(', '.join(temp) + ' мають зкористатися іншим автомобілем')

    def print_passengers_info(self):
        if self.passengers != []:
            print(f"Імена пасажирів {self.brand}: ")
            for passenger in self.passengers:
                print(passenger.name)
        else: print(f"There are no passengers in {self.brand}")
        if self.fuel > 0: print(f"{self.brand} може проїхати: " + str(round(100 / self.consumption * self.fuel)) + " км")
        else: print("Потрібно заправити машину!!!")


nick = Human("Nick")
kate = Human("Kate")
john = Human("John")
sara = Human("Sara")
dora = Human("Dora")
george = Human("George")
ben = Human("Ben")
eva = Human("Eva")
car = Auto("Mercedes", 5, 60, 8)

car.add_passenger(nick, kate, john, sara, dora, george, ben, eva)
print()
print('-' * 20)
print()
car.print_passengers_info()
print()
print('-' * 20)
print()
car.add_fuel(20)
car.print_passengers_info()