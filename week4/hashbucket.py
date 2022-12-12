# Implementing a fixed size hash table in Python that uses bucket hashing. 

class HashBucket:

    def __init__(self, M, B):
        self.M = M         #8                         # table size
        self.B = B         #4                         # number of buckets in the hash table
        self.overFlowArr = [None] * self.M
        self.mainArr = [None] * self.M
        self.slotSize = M // B                         # the slots size of a bucket 

    # hash function
    def produceHash(self, data):      # calculating the slot/index of the data
        sum = 0

        data = str(data)
        for i in data:
            sum += ord(i)
        return sum % self.B             # returns the index

    # Inserts new data in the hash table without duplicates
    def insert(self, data):
        index = self.produceHash(data)

        for value in range((self.slotSize * index), (self.slotSize * (index+1))):
            if (self.mainArr[value] == data):
                return
            
            elif (self.mainArr[value] == None):
                self.mainArr[value] = data
                return

        for value in range(0, len(self.mainArr)):   # same for the overflow array
            if (self.overFlowArr[value] == data):
                return
            
            elif (self.overFlowArr[value] == None):
                self.overFlowArr[value] = data
                return
        return

    # Removes data from the hash table
    def delete(self, data):
        index = self.produceHash(data)

        for value in range((self.slotSize * index), (self.slotSize * (index+1))):
            if (self.mainArr[value] == data):
                self.mainArr[value] = None
                return
            
            elif (self.mainArr[value] == None): # else there isn't the data to be deleted
                return

        for value in range(0, len(self.mainArr)):   # same for the overflow array
            if (self.overFlowArr[value] == data):
                self.overFlowArr[value] = None
                return
            
            elif (self.overFlowArr[value] == None): # else there isn't the data to be deleted
                return
        return

    # prints the hash table and overflow array
    def print(self):
        array = []                          
        
        for item in self.mainArr:
            if (item != None):   # printing the hash table
                array.append(item)
        
        for item in self.overFlowArr:               # printing the overflow array
            if (item != None):
                array.append(item)

        print(*array,sep=" ")   #changing the "," from the array to a " "
        return


if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("MMM123")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("MMM123")
    table.print()   # fOo MMM123 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # MMM123 Bar1 10aaaa1