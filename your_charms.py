# Nathan Wong njw87
# 06/04/2024
# Program Description: To provide a class that can create a charm that represents an Eikon from Final Fantasy XVI and an element

from charm import Charm
from enum import Enum

class EikonicCharm(Charm):
    '''
    Creates a charm that represents an Eikon from Final Fantasy XVI and an element
    
    Parameters:
        Charm (class): The Charm class
    
    Inner Classes:
        Dominant: Assigns an Eikon to each character
        
    Attributes:
        valistheaDict (dictionary): Key-value pairs that tells which nation a character is from
        dominant (EikonicCharm.Dominant): Name of the character
        element (string): An element
        
    Methods:
        __init__: Initializes attributes for EikonicCharm
        getDominant: Return the dominant attribute
        getElement: Returns the element attribute
        getMarketValue: Returns the charm's market value
        setDominant: Sets the value of the dominant attribute if passed argument is of type
        EikonicCharm.Dominant
        elementalBalance: Checks if the charm's Dominant's elemental affinity matches with the charm's element
        __str__: Print the charm's name and Eikon. Ex: "Barnabus - ODIN"
        __lt__: Determines whether this EikonicCharm's market value is less than the other EikonicCharm's
        market value
        __le__: Determines whether this charm's market value is less than or equal to the other
        charm's market value
        __gt__: Determines whether this charm's market value is greater than the other charm's
        market value
        __ge__: Determines whether this charm's market value is greater than or equal to the other charm's
        market value
        __eq__: Determines if the two Dominants are from the same nation
        __ne__: Determines if the two Dominants are not of the same nation
    '''
    valistheaDict = {
            "Dominant.CLIVE" : "ROSARIA",
            "Dominant.JOSHUA" : "ROSARIA",
            "Dominant.JILL" : "NORTHERN TERRITORIES",
            "Dominant.BENEDIKTA" : "WALOED",
            "Dominant.HUGO" : "Dhalmekia",
            "DOMINANT.CID" : "WALOED",
            "Dominant.BARNABUS" : "WALOED",
            "Dominant.DION" : "SANBREQUE"
            }
    class Dominant(Enum):
        '''
        Assigns an Eikon to each character (AKA Dominant)
        
        Parameters:
            Enum (module): Assigns constant values to each Final Fantasy XVI character
        
        Attributes: Dominants assigned with their respective Eikons as a value
        '''
        CLIVE = "IFRIT"
        JOSHUA = "PHEONIX"
        BENEDIKTA = "GARUDA"
        JILL = "SHIVA"
        CID = "RAMUH"
        HUGO = "TITAN"
        BARNABUS = "ODIN"
        DION = "BAHAMUT"
    def __init__(self, name, description, retailPrice, condition, dominant, element):
        '''
        Initializes attributes for EikonCharm object
        
        Parameters:
            self (object): The object itself
            name (string): Name of the charm
            description (string): Description of the charm
            retailPrice (float): Retail price of the charm
            condition (Charm.Condition): Physical condition of the charm
            dominant (EikonicCharm.Dominant): Name of the character
            element (string): An element
            
        Return value: None
        
        Sample call: eikonicCharm = EikonicCharm("Clive", "A man engulfed in flames", 60.00, Charm.Condition.EXCELLENT, EikonicCharm.Dominant.CLIVE, "FIRE")
        '''
        super().__init__(name, description, retailPrice, condition)
        self.__element = element
        self.setDominant(dominant)
    # Getters
    def getDominant(self):
        '''
        Return the dominant attribute
        
        Parameters:
            self (object): The object itself
        
        Return value: The name of the Dominant, in the form of "Dominant.CLIVE"
        
        Sample call: eikon.getDominant()
        '''
        return self.__dominant
    def getElement(self):
        '''
        Returns the element attribute
        
        Parameters:
            self (object): The object itself
            
        Return value: A string representing the charm's element
        
        Sample call: eikon.getElement()
        '''
        return self.__element
    def getMarketValue(self):
        '''
        Returns the charm's market value
        
        Parameters:
            self (object): The object itself
            
        Return value: A float representing the charm's market value
        
        Sample call: charm.getMarketValue()
        '''
        marketValue = float(self.getRetailPrice() * ((self.getCondition().value / 100)+1))
        return round(marketValue, 2)
    # Setter
    def setDominant(self, dominant):
        '''
        Sets the value of the dominant attribute if passed argument is of type
        EikonicCharm.Dominant
        
        Parameters:
            self (object): The object itself
            dominant (EikonicCharm.Dominant): The name of the Dominant
            
        Return value: None
        
        Sample call: charm.setDominant(Dominant.BENEDIKTA)
        '''
        if not isinstance(dominant, EikonicCharm.Dominant):
            raise Exception("Dominant must be of type EikonicCharm.Dominant")
        self.__dominant = dominant
    def elementalBalance(self):
        '''
        Checks if the charm's Dominant's elemental affinity matches with the charm's element
        
        Parameters:
            self (object): The object itself
            
        Return value: Boolean where True if the charm's element matches the Dominant's respective
        elemental affinity (determined based on their Eikon) and returns False otherwise
        
        Sample call: charm.elementalBalance()
        '''
        eikonicDictionary = {
            "Dominant.CLIVE" : ["FIRE", "WIND", "ICE", "LIGHTNING", "EARTH", "DARK", "LIGHT"],
            "Dominant.JOSHUA" : "FIRE",
            "Dominant.BENEDIKTA" : "WIND",
            "Dominant.JILL" : "ICE",
            "Dominant.CID" : "LIGHTNING",
            "Dominant.HUGO" : "EARTH",
            "Dominant.BARNABUS" : "DARK",
            "Dominant.DION" : "LIGHT",
            }
        if self.__element in eikonicDictionary.get(str(self.__dominant)):
            return True
        return False
    # Operator Overloading
    def __str__(self):
        '''
        Print the charm's name and Eikon. Ex: "Barnabus - ODIN"
        
        Parameters:
            self (object): The object itself
            
        Return value: A string containing the charm's name and dominant
        
        Sample call: print(charm)
        '''
        return f"{self.getName()} - {self.__dominant}"
    def __lt__(self, other):
        '''
        Determines whether this EikonicCharm's market value is less than the other EikonicCharm's
        market value
        
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
        Determines if the two Dominants are from the same nation
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
            
        Return value: Boolean where True if the two Dominant's home nations are the same and
        False otherwise
        
        Sample call: print(charm1 == charm2)
        '''
        if self.valistheaDict.get(str(self.__dominant)) == self.valistheaDict.get(str(other.getDominant())):
            return True
        return False
    def __ne__(self, other):
        '''
        Determines if the two Dominants are not of the same nation
        
        Parameters:
            self (object): The object itself
            other (object): The object to be compared against
        
        Return value: Boolean where True if the two Dominants are not from the same nation
        and False otherwise
        
        Sample call: print(charm1 != charm2)
        '''
        if self.valistheaDict.get(str(self.getDominant())) != self.valistheaDict.get(str(other.getDominant())):
            return True
        return False
    
# Hard code testing
if __name__ == "__main__":
    charm = EikonicCharm("Clive", "The man who erased magick from the world of Valisthea", 60.00, Charm.Condition.EXCELLENT, EikonicCharm.Dominant.CLIVE, "FIRE")
    print(charm.elementalBalance())
    charm2 = EikonicCharm("Joshua", "Killed by his own kin", 40.00, Charm.Condition.PRISTINE, EikonicCharm.Dominant.JOSHUA, "FIRE")
    print(charm == charm2)
    print(charm != charm2)
    charm3 = EikonicCharm("CID", "A man dedicated to freeing all Branded", 40.99, Charm.Condition.GOOD, EikonicCharm.Dominant.CID, "LIGHTNING")
    charm4 = EikonicCharm("BENEDIKTA", "A broken woman with unresolved trauma, and Cid's one true love", 40.99, Charm.Condition.DAMAGED, EikonicCharm.Dominant.BENEDIKTA, "WIND")
    print(charm3 == charm4)
    print(charm3 != charm4)
    
