import os
os.system("cls")
class SpaceAircraft:
    def __init__(self, model, height, fuel):
        self.model = model
        self.height = height
        self.fuel = fuel

    def launch(self, km):
        fuel_needed = km * 2
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.height += km
            print(f"{self.model} {km} km ga uchdi. Qolgan yoqilg'i: {self.fuel}")
        else:
            print(f"{self.model} uchun yetarli yoqilg'i yo'q. Qolgan yoqilg'i: {self.fuel}")

    def land(self, km):
        fuel_needed = km
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.height -= km
            print(f"{self.model} {km} km ga qo'ndi. Qolgan yoqilg'i: {self.fuel}")
        else:
            print("No fuel")

spacecraft = SpaceAircraft("Falcon", 0, 100)

spacecraft.launch(20)  
spacecraft.land(20)
