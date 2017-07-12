from car import * 
import unittest 

# class to test the car functionality
class TestCar(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.car = Car()
    
    # function to test the getter and setter functions for colour     
    def testColour(self):
        result = self.car.getColour()
        self.assertEqual('',result)
        
        self.car.setColour('Red')
        result = self.car.getColour()
        self.assertEqual('Red',result)
                        
    # function to test the getter and setter functions for make    
    def testMake(self):
        result = self.car.getMake()
        self.assertEqual('',result)
        
        self.car.setMake('Ferrari')
        result = self.car.getMake()
        self.assertEqual('Ferrari',result)
        
    # function to set the getter and setter functions for mileage 
    def testMileage(self):
        result = self.car.getMileage()
        self.assertEqual(0,result)
        
        self.car.setMileage(20)
        result = self.car.getMileage()
        self.assertEqual(20,result)
      
    # function to test the paint function 
    def testPaint(self):
        self.car.paint('Blue')
        result = self.car.getColour()
        self.assertEqual('Blue', result)
    
    # function to test the move function 
    def testMove(self):
        self.car.move(20)
        result = self.car.getMileage()
        self.assertEqual(20, result)
        
        
# class to test the petrol car functionality
class TestPetrolCar(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.car = PetrolCar()
     
    # function to test the getter and setter functions for colour 
    def testColour(self):
        result = self.car.getColour()
        self.assertEqual('',result)
        
        self.car.setColour('Red')
        result = self.car.getColour()
        self.assertEqual('Red',result)
        
    # function to test the getter and setter functions for make     
    def testMake(self):
        result = self.car.getMake()
        self.assertEqual('',result)
        
        self.car.setMake('Ferrari')
        result = self.car.getMake()
        self.assertEqual('Ferrari',result)
    
    # function to set the getter and setter functions for mileage 
    def testMileage(self):
        result = self.car.getMileage()
        self.assertEqual(0,result)
        
        self.car.setMileage(20)
        result = self.car.getMileage()
        self.assertEqual(20,result)
        
    # function to set the getter and setter functions for number of cylinders    
    def testNumberCylinders(self):
        result = self.car.getNumberCylinders()
        self.assertEqual(1,result)
        
        self.car.setNumberCylinders(2)
        result = self.car.getNumberCylinders()
        self.assertEqual(2,result)
        
    # function to test the paint function 
    def testPaint(self):
        self.car.paint('Blue')
        result = self.car.getColour()
        self.assertEqual('Blue', result)
    
    # function to test the move function 
    def testMove(self):
        self.car.move(20)
        result = self.car.getMileage()
        self.assertEqual(20, result)
        
        
# class to test the petrol car functionality
class TestDieselCar(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.car = DieselCar()
        
    # function to test the getter and setter functions for colour     
    def testColour(self):
        result = self.car.getColour()
        self.assertEqual('',result)
        
        self.car.setColour('Red')
        result = self.car.getColour()
        self.assertEqual('Red',result)
                
    # function to test the getter and setter functions for make      
    def testMake(self):
        result = self.car.getMake()
        self.assertEqual('',result)
        
        self.car.setMake('Ferrari')
        result = self.car.getMake()
        self.assertEqual('Ferrari',result)
        
    # function to set the getter and setter functions for mileage     
    def testMileage(self):
        result = self.car.getMileage()
        self.assertEqual(0,result)
        
        self.car.setMileage(20)
        result = self.car.getMileage()
        self.assertEqual(20,result)
        
    # function to set the getter and setter functions for number of cylinders    
    def testNumberCylinders(self):
        result = self.car.getNumberCylinders()
        self.assertEqual(1,result)
        
        self.car.setNumberCylinders(2)
        result = self.car.getNumberCylinders()
        self.assertEqual(2,result)
        
    # function to test the paint function 
    def testPaint(self):
        self.car.paint('Blue')
        result = self.car.getColour()
        self.assertEqual('Blue', result)
    
    # function to test the move function 
    def testMove(self):
        self.car.move(20)
        result = self.car.getMileage()
        self.assertEqual(20, result)
        
        
# class to test the petrol car functionality
class TestElectricCar(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.car = ElectricCar()
        
    # function to test the getter and setter functions for colour     
    def testColour(self):
        result = self.car.getColour()
        self.assertEqual('',result)
        
        self.car.setColour('Red')
        result = self.car.getColour()
        self.assertEqual('Red',result)
        
    # function to test the getter and setter functions for make      
    def testMake(self):
        result = self.car.getMake()
        self.assertEqual('',result)
        
        self.car.setMake('Ferrari')
        result = self.car.getMake()
        self.assertEqual('Ferrari',result)
        
    # function to set the getter and setter functions for mileage     
    def testMileage(self):
        result = self.car.getMileage()
        self.assertEqual(0,result)
        
        self.car.setMileage(20)
        result = self.car.getMileage()
        self.assertEqual(20,result)
        
    # function to set the getter and setter functions for number of fuel cells   
    def testNumberFuelCells(self):
        result = self.car.getNumberFuelCells()
        self.assertEqual(1,result)
        
        self.car.setNumberFuelCells(2)
        result = self.car.getNumberFuelCells()
        self.assertEqual(2,result)
        
    # function to test the paint function 
    def testPaint(self):
        self.car.paint('Blue')
        result = self.car.getColour()
        self.assertEqual('Blue', result)
    
    # function to test the move function 
    def testMove(self):
        self.car.move(20)
        result = self.car.getMileage()
        self.assertEqual(20, result)
        
   
# class to test the petrol car functionality
class TestHybridCar(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.car = ElectricCar()
        
    # function to test the getter and setter functions for colour    
    def testColour(self):
        result = self.car.getColour()
        self.assertEqual('',result)
        
        self.car.setColour('Red')
        result = self.car.getColour()
        self.assertEqual('Red',result)        
        
    # function to test the getter and setter functions for make      
    def testMake(self):
        result = self.car.getMake()
        self.assertEqual('',result)
        
        self.car.setMake('Ferrari')
        result = self.car.getMake()
        self.assertEqual('Ferrari',result)
        
    # function to set the getter and setter functions for mileage     
    def testMileage(self):
        result = self.car.getMileage()
        self.assertEqual(0,result)
        
        self.car.setMileage(20)
        result = self.car.getMileage()
        self.assertEqual(20,result)
        
    # function to set the getter and setter functions for number of cylinders    
    def testNumberCylinders(self):
        result = self.car.getNumberFuelCells()
        self.assertEqual(1,result)
        
        self.car.setNumberFuelCells(2)
        result = self.car.getNumberFuelCells()
        self.assertEqual(2,result)
        
    # function to set the getter and setter functions for number of fuel cells  
    def testNumberFuelCells(self):
        result = self.car.getNumberFuelCells()
        self.assertEqual(1,result)
        
        self.car.setNumberFuelCells(2)
        result = self.car.getNumberFuelCells()
        self.assertEqual(2,result)
        
    # function to test the paint function 
    def testPaint(self):
        self.car.paint('Blue')
        result = self.car.getColour()
        self.assertEqual('Blue', result)
    
    # function to test the move function 
    def testMove(self):
        self.car.move(20)
        result = self.car.getMileage()
        self.assertEqual(20, result)
        
        
# run only from the command line 
if __name__ == '__main__':

    # runs any subclasses that are preceded by test 
    unittest.main()