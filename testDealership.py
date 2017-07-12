from dealership import * 
import unittest 

# class to test the dealership functionality
class TestDealership(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.dealership = Dealership()
        self.dealership.create_current_stock()
    
    # function to test the totalCars function 
    def testTotalCars(self):
        result = self.dealership.totalCars()
        self.assertEqual(40,result)
    
    # function to test the rentCar function
    def testRentCar(self):
        result = self.dealership.rentCar('Electric',1)
        self.assertEqual('You have rented 1 Electric cars ',result)
        
        # test the totalCars function after a car has been rented
        result = self.dealership.totalCars()
        self.assertEqual(39,result)
        
        # test the rent function for an amount greater than the total 
        result = self.dealership.rentCar('Hybrid',5)
        self.assertEqual('Not enough cars in stock',result)

    # function to test the returnCar function 
    def testReturnCar(self):
        self.dealership.rentCar('Electric',1)
        
        # test the checkRental function 
        result = self.dealership.checkRentals('Electric')
        self.assertEqual(0,result)
        result = self.dealership.checkRentals('Petrol')
        self.assertEqual(-1,result)
        
        # test the returnCar function 
        result = self.dealership.returnCar('Diesel')
        self.assertEqual('No diesel cars currently on rental',result)
        result = self.dealership.returnCar('Electric')
        self.assertEqual('You have returned the car',result) 

    def testCheckRentals(self):
        result = self.dealership.checkRentals('Petrol')
        self.assertEqual(-1,result)
        
        self.dealership.rentCar('Petrol',1)
        result = self.dealership.checkRentals('Petrol')
        self.assertEqual(0,result)
        
        
                
        
# run only from command line 
if __name__ == '__main__':

    # runs any methods that are preceded by test
    unittest.main()
        
    