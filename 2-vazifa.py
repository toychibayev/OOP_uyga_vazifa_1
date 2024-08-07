import os
os.system("cls")

class MinutesConverter:
    def toHours(self, minutes: int):
        return minutes / 60
    def toSeconds(self, minutes: int):
        return minutes * 60
    def toDays(self, minutes: int):
        return minutes / (60 * 24)

natija = MinutesConverter()

minutes = int(input("Minutni kiriting: "))

print(natija.toHours(minutes)," Soat")
print(natija.toSeconds(minutes),"Sekund")
print(natija.toDays(minutes),"Kun")
