#Jesse Como
#100656363

from house import House
from apartment import Apartment

def main():
    house = House("House", 160000, 12, "231 Chestnut Street", 3)
    house.printData()
    print("Get Dwelling Type: ", house.get_dwellingType())
    print(house)

    apartment = Apartment("Apartment", 75000, 2, "12 Simcoe Street", 14)
    apartment.printData()
    print("Get Dwelling Type: ", apartment.get_dwellingType())
    print(apartment)

main()