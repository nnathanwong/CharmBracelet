# Nathan Wong njw87
# 06/04/2024
# Program Description: To simulate the creation of a friendship charm

from charm import Charm

class FriendshipCharm(Charm):
    '''
    Creates a friendship charm for a bracelet
    
    Parameters:
        Charm (class): The Charm class
    
    Attributes:
        symbol (string): A character representing the charm
    
    Methods:
        __init__: Initializes FriendshipCharm's attributes
        getMarketValue: Returns the market value of the charm
        getSymbol: Returns the symbol of the charm
        __str__: Returns the value stored in symbol
        __lt__: Determines which of the two friendship_charm objects has the least market value
        __le__: Determines which of the two friendship_charm objects has the least market value or if their
        market values are of equal value
        __gt__: Determines which of the two friendship_charm objects has the greatest market value
        __ge__: Determines which of the two friendship_charm objects have the greatest market value or if their
        respective market value's are of equal value
        __eq__: Determines whether the two friendship_charm objects' market value are of equal value
        __ne__: Determines whether the two friendship_charm objects' market value are not equal value
    '''
    # Constructor
    def __init__(self, name, description, retailPrice, condition, symbol):
        '''
        Instantiates a FriendshipCharm object with its attributes
        
        Parameters:
            self (object): The object itself
            name (string): The name of the charm
            retailPrice (float): The retail price of the charm
            condition (Charm.Condition): The condition of the charm referenced by dot notation of the inner
            class, "Condition"
            symbol (string): A character representing the charm
        
        Return value: None
        
        Sample call: charm = FriendshipCharm("Boot", "A charm from Texas", 5.95, Charm.Condition.PRISTINE, "A")
        '''
        super().__init__(name, description, retailPrice, condition)
        self.__symbol = symbol
    # Getters
    def getMarketValue(self):
        '''
        Returns the market value of the charm
        
        Parameters:
            self (object): The object itself
            
        Return value: A float representing the market value of the charm
        
        Sample call: charm.getMarketValue()
        '''
        marketValue = float(self.getCondition().value / 100)
        return round(marketValue, 2)
    def getSymbol(self):
        '''
        Returns the symbol of the charm
        
        Parameters:
            self (object): The object itself
            
        Return value: A string that represents the symbol (character) of the charm
        
        Sample call: charm.getSymbol()
        '''
        return self.__symbol
    # Operator Overloading
    def __str__(self):
        '''
        Prints the value stored in symbol
        
        Parameters:
            self (object): The object itself
        
        Return value: A string that represents the symbol (character) of the charm
        
        Sample call: print(charm)
        '''
        return self.__symbol
    def __lt__(self, other):
        '''
        Determines which of the two friendship_charm objects has the least market value
        
        Parameters:
            self (object): The object itself
            other (object): The object to compare the self object to
            
        Return value: A Boolean value where True means that self's market value is less than other and False means
        that self's market value is not less than other
        
        Sample call: print(charm < charm2)
        '''
        return (self.getMarketValue() < other.getMarketValue())
    def __le__(self, other):
        '''
        Determines which of the two friendship_charm objects has the least market value or if their
        market values are of equal value
        
        Parameters:
            self (object): The object itself
            other (object): The object to compare the self object to
            
        Return value: A Boolean value where True means that self's market value is less than or equal
        to other's market value and False means that self's market value is not less than or equal to other's
        market value
        
        Sample call: print(charm <= charm2)
        '''
        return (self.getMarketValue() <= other.getMarketValue())
    def __gt__(self, other):
        '''
        Determines which of the two friendship_charm objects has the greatest market value
        
        Parameters:
            self (object): The object itself
            other (object): The object to compare the self object to
            
        Return value: A Boolean value where True means that self's market value is greater than other's
        market value and False means that self's market value is not greater than other's
        
        Sample call: print(charm > charm2)
        '''
        return (self.getMarketValue() > other.getMarketValue())
    def __ge__(self, other):
        '''
        Determines which of the two friendship_charm objects have the greatest market value or if their
        respective market value's are of equal value
        
        Parameters:
            self (object): The object itself
            other (object): The object to compare the self object to
        
        Return value: A Boolean value where True means that self's market value is greater than or equal
        to other's market value and False means that self's market value is not greater than or equal to other's
        market value
        
        Sample call: print(charm >= charm2)
        '''
        return (self.getMarketValue() >= other.getMarketValue())
    def __eq__(self, other):
        '''
        Determines whether the two friendship_charm objects' market value are of equal value
        
        Parameters:
            self (object): The object itself
            other (object): The object to compare the self object to
            
        Return value: A Boolean value where True means that the objects' market value are equal and False means
        that the objects' market value are not equal to each other
        
        Sample call: print(charm == charm)
        '''
        return (self.getMarketValue() == other.getMarketValue())
    def __ne__(self, other):
        '''
        Determines whether the two friendship_charm objects' market value are not equal value
        
        Parameters:
            self (object): The object itself
            other (object): The object to compare the self object to
            
        Return value: A Boolean value where True means that the objects' market values are not equal
        and False means that their market values are equal to each other
        
       Sample call: print(charm != charm2)
       '''
        return (self.getMarketValue() != other.getMarketValue())