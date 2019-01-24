#Jesse Como
#100656363

from dwelling import Dwelling
class Apartment(Dwelling):
    def __init__(self, typeOfDwelling, value, rooms, address, apartmentNumber):
        super().__init__(typeOfDwelling, value, rooms)
        self.__address = address
        self.__apartmentNumber = apartmentNumber

    def printData(self):
        print(super(Apartment, self).printData(), "\nAddress: ", self.__address, "\nApartment Number: ", self.__apartmentNumber)

    def __str__(self):
        return "{}Address: {}\nApartment Number: {}\n".format(super().__str__(), self.__address, self.__apartmentNumber)