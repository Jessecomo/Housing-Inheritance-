#Jesse Como
#100656363

class Dwelling:
    def __init__(self, typeOfDwelling, value, rooms):
        self.__typeOfDwelling = typeOfDwelling
        self.__value = value
        self.__rooms = rooms

    def printData(self):
        print("Type of Dwelling: ", self.__typeOfDwelling, "\nValue: ", self.__value, "\nRooms: ", self.__rooms)

    def get_dwellingType(self):
        return self.__typeOfDwelling

    def __str__(self):
        return "Type of Dwelling: {}\nValue: {}\nRooms: {}\n".format(self.__typeOfDwelling, self.__value, self.__rooms)