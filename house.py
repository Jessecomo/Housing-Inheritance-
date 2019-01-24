#Jesse Como
#100656363

from dwelling import Dwelling
class House(Dwelling):
    def __init__(self, typeOfDwelling, value, rooms, address, numOfFloors):
        super().__init__(typeOfDwelling, value, rooms)
        self.__address = address
        self.__numOfFloors = numOfFloors

    def printData(self):
        print(super(House, self).printData(), "\nAddress: ", self.__address, "\nNumber of Floors: ", self.__numOfFloors)

    def __str__(self):
        return "{}Address: {}\nNumber of Floors: {}\n".format(super().__str__(), self.__address, self.__numOfFloors)