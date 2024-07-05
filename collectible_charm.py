# Nathan Wong njw87
# 06/04/2024
# Program Description: To provide a class that creates a collectible charm for a bracelet

from charm import Charm

class CollectibleCharm(Charm):
    '''
    Creates a collectible charm for a bracelet
    
    Parameters:
        Charm (class): The Charm class
    
    Attributes:
        serialNumber (string): Serial number of the collectible charm
        
    Methods:
        __init__: Initializes CollectibleCharm's attributes
        getSerialNumber: Returns the collectible charm instance's serial number
        getMarketValue: Returns the charm's market value
        __str__: Print the charm's name and serial number
        __lt__: Determines whether this CollectibleCharm's market value is less than the other
        CollectibleCharm's market value
        __le__: Determines whether this charm's market value is less than or equal to the other
        charm's market value
        __gt__: Determines whether this charm's market value is greater than the other charm's
        market value
        __ge__: Determines whether this charm's market value is greater than or equal to the other charm's
        market value
        __eq__: Determines whether this charm is the same charm as the other charm
        __ne__: Determines whether this charm is different from the other charm
    '''
    def __init__(self, name, description, retailPrice, condition, serialNumber):
        '''
        Initializes CollectibleCharm's attributes
        
        Parameters:
            self (object): The object itself
            name (string): Name of the charm
            description (string): Description of the charm
            retailPrice (float): Retail price of the charm
            condition (Charm.Condition): Physical condition of the charm
            serialNumber (string): Serial number of the charm
        
        Return value: None
        
        Sample call: collectCharm = CollectibleCharm("Charm", "A charm", 90.95, Charm.Condition.EXCELLENT, "G585-037")
        '''
        super().__init__(name, description, retailPrice, condition)
        self.__serialNumber = serialNumber
    # Getters
    def getSerialNumber(self):
        '''
        Returns the collectible charm instance's serial number
        
        Parameters:
            self (object): The object itself
            
        Return value: A string representing the object's serial number
        
        Sample call: collectCharm.getSerialNumber()
        '''
        return self.__serialNumber
    def getMarketValue(self):
        '''
        Returns the charm's market value
        
        Parameters:
            self (object): The object itself
            
        Return value: A float representing the charm's market value
        
        Sample call: charm.getMarketValue()
        '''
        marketValue = float(self.getRetailPrice() * (self.getCondition().value / 100))
        return round(marketValue, 2)
    # Operator overloading
    def __str__(self):
        '''
        Print the charm's name and serial number. Ex: "Cherry Blossom Dangle [G585-037]"
        
        Parameters:
            self (object): The object itself
            
        Return value: A string containing the charm's name and serial number
        
        Sample call: print(charm)
        '''
        return f"{self.getName()} [{self.__serialNumber}]"
    def __lt__(self, other):
        '''
        Determines whether this CollectibleCharm's market value is less than the other
        CollectibleCharm's market value
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
        
        Return value: A Boolean value; True if self's market value is less than other's; False if self's
        market value is not less than other's
        
        Sample call: print(charm1 < charm2)
        '''
        return (self.getMarketValue() < other.getMarketValue())
    def __le__(self, other):
        '''
        Determines whether this charm's market value is less than or equal to the other
        charm's market value
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
            
        Return value: A Boolean value; True if self is less than or equal to other's market value;
        False if self's market value is not less than or equal to other's market value
        
        Sample call: print(charm <= charm2)
        '''
        return (self.getMarketValue() <= other.getMarketValue())
    def __gt__(self, other):
        '''
        Determines whether this charm's market value is greater than the other charm's
        market value
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
            
        Return value: Boolean where true if self's market value is greater than other's and false
        is self's market value is not greater than other's
        
        Sample call: print(charm > charm2)
        '''
        return (self.getMarketValue() > other.getMarketValue())
    def __ge__(self, other):
        '''
        Determines whether this charm's market value is greater than or equal to the other charm's
        market value
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
        
        Return value: Boolean where true if self's market value is greater than or equal to other's and
        false is self's market value is not greater than or equal to other's
        
        Sample call: print(charm >= charm2)
        '''
        return (self.getMarketValue() >= other.getMarketValue())
    def __eq__(self, other):
        '''
        Determines whether this charm is the same charm as the other charm
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
            
        Return value: Boolean where true if self's attributes match exactly with other's attributes;
        False is self's attributes do not match exactly with other's
        
        Sample call: print(charm == charm2)
        '''
        if self.getName() != other.getName():
            return False
        if self.getDescription() != other.getDescription():
            return False
        if self.getRetailPrice() != other.getRetailPrice():
            return False
        if self.getCondition() != other.getCondition():
            return False
        if self.__serialNumber != other.getSerialNumber():
            return False
        return True
    def __ne__(self, other):
        '''
        Determines whether this charm is different from the other charm
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
            
        Return value: Boolean where true if self's attributes do not match with other's and false if
        self's attributes match exactly with other's attributes
        
        Sample call: print(charm != charm2)
        '''
        if self.getName() != other.getName():
            return True
        if self.getDescription() != other.getDescription():
            return True
        if self.getRetailPrice() != other.getRetailPrice():
            return True
        if self.getCondition() != other.getCondition():
            return True
        if self.__serialNumber != other.getSerialNumber():
            return True
        return False