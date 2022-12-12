# Implementing a fixed sized hash table in Python
# The in this case fixed size hash table stores str values and the hash value (slot) is calculated in the
# produceHash method

class HashLinear:

    def __init__(self, M):
        self.M = M              # table size
        self.T = [None] * M     # "empty" table

    def produceHash(self, data):      # calculating the slot/index of the data
        sum = 0
        for i in data:
            sum += ord(i)
        return sum % self.M             # returns the index

    def insert(self, data):             
        counter = 0 
        index = self.produceHash(data)          

        while (counter <= self.M): 
            if (self.T[index] == data):
                break
            
            elif ((self.T[index] == None) or (self.T[index] == -1)): 
                self.T[index] = data
                break
            
            if (index+1 == self.M):
                index = 0

            else: 
                index += 1
            counter += 1

    def delete(self, data):
        counter = 0
        index = self.produceHash(data)

        while(self.T[index] != None):

            if (self.T[index] == data):
                self.T[index] = -1
                break

            if (index+1 == self.M):
                index = 0

            else: 
                index += 1
            counter += 1

    def print(self):            # adding the values to an array so it's easier to print
        array = []                          
        
        for item in self.T:
            if ((item != -1) and (item != None)):
                array.append(item)
        
        print(*array,sep=" ")   # changing the "," from the array to a " "

        return


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("MMM123")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("MMM123")
    table.print()   # 10aaaa1 MMM123 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 MMM123 Bar1