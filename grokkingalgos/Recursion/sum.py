#!/usr/bin/python3.11
"""
    @name sum.py
    @purpose Demonstrate a summing using recursion. 
"""
import random
class List:
    def __init__(self, myList:list):
        self.myList = myList
    
    def get(self):
        return self.myList
    
    def set(self, newValue):
        self.myList.append(newValue)
   
    @staticmethod
    def view(myList):
        print(myList)
    
    @staticmethod
    def createRandValues(nItems=10):
        """
            @method createRandValues()
            @purpose create random integers values up to n items.
            @param nItems: Integer | the size of the set.
            @return newArray
        """
        randValues = set()
        for item in range(nItems):
            randValue = random.randint(1,10_000)
            randValues.update( {randValue} )
        return list(randValues)

    @staticmethod
    def sum(myList):
        """
            @method sum()
            @param myList: List
            @purpose 
            @return
        """
        emptyArray = (len(myList) == 0)
        soloArray = (len(myList) == 1)
        baseCase = emptyArray or soloArray
        if baseCase:
            if emptyArray: 
                return 0
            else: 
                return myList[0]
        else:
            recursiveCase = myList[0] + sum(myList[1:])
            return recursiveCase
    
    @staticmethod
    def size(myList):
        """
            @method size()
            @param myList: List
            @purpose 
            @return
        """
        baseCase = len( myList ) == 0
        if baseCase: 
            return 0
        else:
            recursiveCase = (1) + len(myList[1:])
            return recursiveCase
   
    @staticmethod
    def max(myList):
        """
            @method max()
            @param myList: List
            @purpose 
            @return
        """
        baseCase = ( len( myList ) == 2 )
        if baseCase:
            elementZeroIsGreater = (myList[ 0 ] > myList[ 1 ] )
            if elementZeroIsGreater:
                return myList[ 0 ]
            else:
                return myList[ 1 ]
        else:
            subMax = max( myList[ 1: ] )
            elementZeroIsMax = (myList[ 0 ] > subMax)
            if elementZeroIsMax:
                recursiveCase = myList[ 0 ]
            else:
                recursiveCase = subMax
            return recursiveCase
   
if __name__ == "__main__":
    testList = List.createRandValues(12)
    List.view(testList)
    listSum = List.sum(testList); print("Sum of list:", listSum)
    listSize = List.size(testList); print("Size of list:", listSize)
    listMax = List.max(testList); print("List's Max:", listMax)