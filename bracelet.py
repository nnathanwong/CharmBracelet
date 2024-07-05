# Nathan Wong
# 06/04/2024
# Program Description: To provide a class for a bracelet that has charms on it

from linked_list import LinkedList
from linked_list import Node
from charm import Charm
from friendship_charm import FriendshipCharm
from collectible_charm import CollectibleCharm
from your_charms import EikonicCharm

class Bracelet(LinkedList):
    '''
    Creates a bracelet that has charms on it
    
    Attributes:
        marketValue (float): The bracelet's market value, inputted by the user
        
    Methods:
        __init__: Initializes Bracelet object with attributes and invokes LinkedList
        isOpen: Checks if the bracelet is open
        isClosed: Checks if the bracelet is closed
        append: Adds a charm to the bracelet
        getMarketValue: Returns the market value of the bracelet overall (including its charms)
        close: Makes the bracelet loop together (creates a doubly-linked list)
        open: Makes the bracelet unloop itself (creates a singly-linked list)
        remove: Removes a charm from the bracelet
        search: Searches for a charm in the bracelet
    '''
    def __init__(self, marketValue):
        '''
        Initializes Bracelet object with attributes and invokes LinkedList
        
        Parameters:
            self (object): The object itself
            marketValue (float): The market value of the bracelet inputted by the user
            
        Return value: None
        
        Sample call: bracelet = Bracelet(20)
        '''
        super().__init__()
        self.__marketValue = marketValue
    def isOpen(self):
        '''
        Checks if the bracelet is open
        
        Parameters:
            self (object): The object itself
            
        Return value: Boolean where True if the bracelet is empty or if the last charm's getNext() points to a "None" node;
        False if the last charm's getNext() points to the head node
        
        Sample call: bracelet.isOpen()
        '''
        if super().isEmpty():
            return True
        head = super().getHead()
        current = head
        while True:
            if current.getNext() == head:
                return False
            if current.getNext() == None:
                return True
            else:
                current = current.getNext()
    def isClosed(self):
        '''
        Checks if the bracelet is closed
        
        Parameters:
            self (object): The object itself
            
        Return value: Boolean where True if the bracelet is closed; False if the bracelet does not have any charms or if
        getNext() points to None
        
        Sample call: bracelet.isClosed()
        '''
        if super().isEmpty():
            return False
        head = super().getHead()
        current = head
        while True:
            if current.getNext() == head:
                return True
            if current.getNext() == None:
                return False
            else:
                current = current.getNext()
    def append(self, data):
        '''
        Adds a charm to the bracelet
        
        Parameters:
            self (object): The object itself
            data (object): A charm object
        
        Return value: 0 if data cannot be appended
        
        Sample call: bracelet.append(charm4)
        '''
        if super().isEmpty() == False:
            if isinstance(data, Charm) and self.isClosed() == False:
                super().append(data)
            elif isinstance(data, Charm):
                self.open()
                super().append(data)
                self.close()
        elif isinstance(data, Charm):
            super().append(data)
        else:
            return 0
    def appraise(self):
        '''
        Returns the market value of the bracelet overall (including its charms)
        
        Parameters:
            self (object): The object itself
            
        Return value: A float representing the bracelet and charms' market value combined
        
        Sample call: bracelet.appraise()
        '''
        charmMarketValue = 0
        head = super().getHead()
        current = head
        if self.isOpen():
            while current != None:
                charmMarketValue += current.getData().getMarketValue()
                current = current.getNext()
        else:
            while current.getNext() != head:
                charmMarketValue += current.getData().getMarketValue()
                current = current.getNext()
        return round(float(charmMarketValue + self.__marketValue), 2)
    def close(self):
        '''
        Makes the bracelet loop together (creates a doubly-linked list)
        
        Parameters:
            self (object): The object itself
            
        Return value: None
        
        Sample call: bracelet.close()
        '''
        head = super().getHead()
        if super().isEmpty() or self.isClosed():
            return
        current = head
        found = False
        while found == False:
            if current.getNext() == None:
                current.setNext(head)
                found = True
            else:
                current = current.getNext()
    def open(self):
        '''
        Makes the bracelet unloop itself (creates a singly-linked list)
        
        Parameters:
            self (object): The object itself
        
        Return value: None
        
        Sample call: bracelet.open()
        '''
        head = super().getHead()
        if super().isEmpty() or self.isOpen():
            return
        current = head
        found = False
        while found == False:
            if current.getNext() == head:
                current.setNext(None)
                found = True
            else:
                current = current.getNext()
    def remove(self, item):
        '''
        Removes a charm from the bracelet
        
        Parameters:
            self (object): The object itself
            item (object): A charm object
            
        Return value: True if the charm object was removed and False if was not found/not removed
        
        Sample call: bracelet.remove(charm)
        '''
        if self.isClosed():
            self.open()
            removed = super().remove(item)
            self.close()
        else:
            removed = super().remove(item)
        return removed
    def search(self, item):
        '''
        Searches for a charm in the bracelet
        
        Parameters:
            self (object): The object itself
            item (object): A charm object
            
        Return value: Boolean True if charm was found and False otherwise
        
        Sample call: bracelet.search(charm)
        '''
        if self.isClosed():
            self.open()
            search = super().search(item)
            self.close()
        else:
            search = super().search(item)
        return search
    
# Demonstration on how to use    
if __name__ == "__main__":
    charm1 = FriendshipCharm("Boot", "A charm from Texas", 5.95, Charm.Condition.PRISTINE, "A")
    charm2 = CollectibleCharm("Charm", "A charm", 90.95, Charm.Condition.EXCELLENT, "G585-037")
    charm3 = EikonicCharm("Clive", "A man engulfed in flames", 60.00, Charm.Condition.EXCELLENT, EikonicCharm.Dominant.CLIVE, "FIRE")
    charm4 = EikonicCharm("BENEDIKTA", "A broken woman with unresolved trauma, and Cid's one true love", 40.99, Charm.Condition.DAMAGED, EikonicCharm.Dominant.BENEDIKTA, "WIND")
    charm5 = charm2 = EikonicCharm("Joshua", "Killed by his own kin", 40.00, Charm.Condition.PRISTINE, EikonicCharm.Dominant.JOSHUA, "FIRE")
    bracelet = Bracelet(20)
    bracelet.append(charm1)
    bracelet.append(charm2)
    bracelet.append(charm3)
    print("Total market value:", bracelet.appraise())
    bracelet.close()
    bracelet.open()
    print("Open:", bracelet.isOpen())
    bracelet.append(charm4)
    bracelet.close()
    bracelet.close()
    bracelet.append(charm5) 
    print("Total market value:", bracelet.appraise())
    print("Open:", bracelet.isOpen())
    print("Close:", bracelet.isClosed())
    print(bracelet.remove(charm4))
    print(bracelet.remove(charm4))
    print(bracelet.remove(charm5))
    
    