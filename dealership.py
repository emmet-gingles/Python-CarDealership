from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar 

# Define a class for dealership
class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrids = []
        self.rental_cars = []
     
    # function that adds stock of cars to each array
    def create_current_stock(self):       
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range(8):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(4):
           self.hybrids.append(HybridCar())
           
    # function that returns the total number of cars available to rent        
    def totalCars(self):
        cars = len(self.petrol_cars) + len(self.diesel_cars) + len(self.electric_cars) + len(self.hybrids)
        return cars
        

    # function that allows customer to rent a car 
    def rentCar(self, carType, amount):
        car_list = []
        # uses car type to decide what array to use 
        if carType == 'Petrol':
            car_list = self.petrol_cars
        elif carType == 'Diesel':
            car_list = self.diesel_cars
        elif carType == 'Electric':
            car_list = self.electric_cars
        elif carType == 'Hybrid':
            car_list = self.hybrids
      
        # if the length of the array is less than the amount entered then return an error
        if len(car_list) < amount:
            return 'Not enough cars in stock'
            
        total = 0
        # pops cars off the array based on the amount 
        while total < amount:
            car_list.pop()
            total = total + 1        
        
        # use car type to decide what type of car to add to the rentals
        if carType == 'Petrol':
             self.rental_cars.append('Petrol')
        elif carType == 'Diesel':
            self.rental_cars.append('Diesel')
        elif carType == 'Electric':
            self.rental_cars.append('Electric')
        elif carType == 'Hybrid':
            self.rental_cars.append('Hybrid')
        return 'You have rented ' + str(amount) + ' ' + carType + ' cars '      
           
       
    # function that allows customer to return a car    
    def returnCar(self, carType): 
        # checks car type 
        if carType == 'Petrol':
            # call checkRentals function to determine whether or not the car type is on rentals
            index = self.checkRentals('Petrol')
            # if car type is in rentals then remove it from rentals and add it to the associated array
            if index != -1:
                self.rental_cars.pop(index)
                self.petrol_cars.append(PetrolCar())
                return 'You have returned the car'
            # else car type is not in rentals 
            else:
                return 'No petrol cars currently on rental'
        elif carType == 'Diesel':
            index = self.checkRentals('Diesel')
            if index != -1:
                self.rental_cars.pop(index)
                self.petrol_cars.append(DieselCar())
                return 'You have returned the car'
            else:
                return 'No diesel cars currently on rental'
        elif carType == 'Electric':
            index = self.checkRentals('Electric')
            if index != -1:
                self.rental_cars.pop(index)
                self.petrol_cars.append(ElectricCar())
                return 'You have returned the car'
            else:
                return 'No electric cars currently on rental'
        elif carType == 'Hybrid':
            index = self.checkRentals('Hybrid')
            if index != -1:
                self.rental_cars.pop(index)
                self.petrol_cars.append(HybridCar())
                return 'You have returned the car'
            else:
                return 'No hybrids currently on rental'
                    
    # function that checks that a car type is currently on rental         
    def checkRentals(self, carType):
        # checks rentals for the car type, if it found it returns the position 
        if carType in self.rental_cars:
            pos = self.rental_cars.index(carType)
            return pos   
        # else car type is not in rentals 
        else:
            return -1
            
            
# called only from command line 
if __name__ == '__main__':

    # instance of dealership object
    dealership = Dealership()
    # create stock of cars
    dealership.create_current_stock()

    # continue loop until user breaks out 
    while True:
        answer = raw_input('Would you like to rent a car? Y/N: ')
        # if user inputs positively
        if answer.upper() == 'Y' or answer.upper() == 'YES':
            # inform the user how many cars are available to rent 
            carsAvailable = dealership.totalCars()
            print 'available cars ', carsAvailable
            # if no cars are available then print message 
            if carsAvailable == 0:
                print 'Sorry nothing to rent, please try again'
            else:
                carType = None 
                while True:
                    # allow user to input the car they would like 
                    carType = raw_input('''What type of car?
                    1. Petrol
                    2. Diesel 
                    3. Electric 
                    4. Hybrid
                    ''')
                    # try to cast input to an integer
                    try:
                        carType = int(carType)
                        # use number to determine the car type 
                        if carType == 1:
                            print 'You selected a petrol car'
                            carType = 'Petrol'
                            break
                        elif carType == 2:
                            print 'You selected a diesel car'
                            carType = 'Diesel'
                            break 
                        elif carType == 3:
                            print 'You selected an electric car'
                            carType = 'Electric'
                            break 
                        elif carType == 4:
                            print 'You selected a hybrid'
                            carType = 'Hybrid'
                            break 
                        # if number input is less than 1 or greater than 4 
                        else:
                            print 'Please enter a number between 1 and 4'
                    # if not print exception
                    except:
                        print 'Invalid input'
                while True:
                    # allow user to input the amount of cars they would like to rent 
                    amount = raw_input('How many would you like?: ')
                    # try to cast input to an integer
                    try:
                        amount = int(amount)                       
                    # if not print exception
                    except: 
                        print 'Please enter a number'
                    # if amount is zero or a negative number 
                    if amount < 1:
                        print 'Amount must be greater than zero'
                    # if no exception then call rentCar function 
                    else:
                        print dealership.rentCar(carType,amount)
                        break 
                # allow the user the option to continue or exit the program 
                answer = raw_input('Do you wish to continue? Y/N: ')
                if answer.upper() == 'N' or answer.upper() == 'NO':
                    print 'Thank you, come again'
                    break
                    
        # else if user inputs negatively 
        elif answer.upper() == 'N' or answer.upper() == 'NO':
            # ask the user if they would like to return a car 
            answer = raw_input('Would you like to return a car? Y/N: ')
            # if user inputs positively
            if answer.upper() == 'Y' or answer.upper() == 'YES':
                # check that number of cars currently on rental is greater than zero 
                if len(dealership.rental_cars) > 0:
                    while True:
                        # allow user to input the car they would like 
                        carType = raw_input('''What type of car
                        1. Petrol
                        2. Diesel 
                        3. Electric 
                        4. Hybrid 
                        ''')
                        # try to cast input to an integer
                        try:
                            carType = int(carType)
                            if carType == 1:
                                carType = 'Petrol'                      
                                break
                            elif carType == 2:
                                carType = 'Diesel'
                                break 
                            elif carType == 3:
                                carType = 'Electric'
                                break
                            elif carType == 4:
                                carType = 'Hybrid'
                                break
                            else:
                                print 'Enter number between 1 and 4'
                        except:
                            print 'Invalid input'
                    # call the returnCar function 
                    print dealership.returnCar(carType)
                    # allow user the option to continue or exit the program 
                    answer = raw_input('Do you wish to continue? Y/N: ')
                    if answer.upper() == 'N' or answer.upper() == 'NO':
                        print 'Thank you, come again'
                        break
                # else no cars currently on rental
                else:
                    print 'No cars currently out on rental'
            # else if user input negatively, allow user the option to continue or exit the program     
            elif answer.upper() == 'N' or answer.upper() == 'NO':
                answer = raw_input('Do you wish to continue? Y/N: ')
                if answer.upper() == 'N' or answer.upper() == 'NO':
                    print 'Thank you, come again'
                    break 
        
    

