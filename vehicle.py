#Emily Dennis 
#14/04/19

#creates the Vehicle class
class Vehicle:
    #initialises the class
    #@param registration by default is set
    def __init__(self, registration):
        self._registration= registration
        self._make="none"
        self._enginesize="none"
        #self variables set
    
    # Sets the value of self._registration
    #@param registration passed
    def setRegistration(self,registration):
        self._registration=registration

    # Gets self._registration
    def getRegistration(self):
        return self._registration

    # Sets the value of self._make
    #@param make passed
    def setMake(self,make):
        self._make= make
        
    # Gets self._make
    def getMake(self):
        return self._make
    
    # Sets the value of self._enginesize
    #@param engine size passed
    def setEngineSize(self,engineSize):
        self._enginesize =engineSize
        
    # Implement this method
    def getEngineSize(self):
        return self._enginesize
    
    # prints the return in specified format using repr, uses string formatting

    def __repr__(self):
        return ("\nVehicle Registration:" + self._registration+ "\nMake:"+ self._make+ "\nEngine size:"+ str(self._enginesize))
#creates the Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self,Registration):
        super().__init__(Registration)
        self._seats = "None"

    
    # Sets the value of self._seats
    #@param seats is passed
    def setNumberOfSeats(self,seats):
        self._seats = seats
    #gets the number of seats
    def getNumberOfSeats(self):
        return self._seats

    #inherits from vehicle repr and adds number of seats

    def __repr__(self):
        return super().__repr__()+ ("\nNumber of seats:" + str(self._seats))
        
#creates the Motorcycle class inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self,Registration):
        super(). __init__(Registration)
        self._offRoad = "None"
        
    # Sets the value of self._offRoad
    #@param offroad passed in
    def setDrivableOffRoad(self,offRoad):
        self._offRoad = offRoad
    #gets self._offroad
    def getDrivableOffRoad(self):
        return str(self._offRoad)
    
    #inherits from vehicle repr and adds drivable off road

    def __repr__(self):
        return super().__repr__()+ ("\nDrivable Off Road:" + str(self._offRoad))
        
    
    
