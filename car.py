# Define a class for car 
class Car(object):
    
    # set up class and variables 
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        
    # function that returns the colour 
    def getColour(self):
        return self.__colour

    # function that returns the make 
    def getMake(self):
        return self.__make

    # function that returns the mileage 
    def getMileage(self):
        return self.__mileage

    # function that sets the colour
    def setColour(self, colour):
        self.__colour = colour

    # function that sets the make 
    def setMake(self, make):
        self.__make = make

    # function that sets the mileage 
    def setMileage(self, mileage):
        self.__mileage = mileage

    # function that changes the car colour 
    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    # function that moves car and increases mileage 
    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
        
# Define a class for electric car         
class ElectricCar(Car):

    # set up class as subclass of Car 
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    # function that returns the number of fuel cells
    def getNumberFuelCells(self):
        return self.__numberFuelCells

    # function that sets the number of fuel cells 
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

# Define a class for petrol car        
class PetrolCar(Car):

    # set up class as subclass of Car
    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    # function that returns the number of cylinders
    def getNumberCylinders(self):
        return self.__numberCylinders

    # function that sets the number of cylinders
    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
# Define a class for diesel car         
class DieselCar(Car):

    # set up class as subclass of Car
    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    # function that returns the number of cylinders
    def getNumberCylinders(self):
        return self.__numberCylinders

    # function that sets the number of cylinders
    def setNumberCylinders(self, value):
        self.__numberCylinders = value
 
# Define a class for hybrid car  
class HybridCar(Car):

    # set up class as subclass of Car
    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1
        self.__numberFuelCells = 1

    # function that returns the number of cylinders
    def getNumberCylinders(self):
        return self.__numberCylinders

    # function that sets the number of cylinders
    def setNumberCylinders(self, value):
        self.__numberCylinders = value
     
    # function that returns the number of fuel cells
    def getNumberFuelCells(self):
        return self.__numberFuelCells

    # function that sets the number of fuel cells
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value