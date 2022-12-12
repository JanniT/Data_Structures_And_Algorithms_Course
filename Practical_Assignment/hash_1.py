import time
import random

class Node: 
    def __init__(self, data):  #Initializing the nodes 
        self.data = data
        self.next = None

class hashTable:

    def __init__(self, M):
        self.tableSize = M              #Table size
        self.linkedLists = [Node(None) for i in range(self.tableSize)]     #Creating the (empty) list containing linked lists

    # Hash function
    def produceHash(self, data):    # Calculating the slot/index of the data
        sum = 0
        data = str(data)
        for i in data:
            sum += ord(i)**ord(i)   # Ord() gets the unicode for the characters
        # print(sum) 
        return sum % self.tableSize 

    # Inserting a item/value to the hashtable
    def insert(self, data):       
        hash_index = self.produceHash(data)  # Calling method that does the hash
        newNode = Node(data)                        # newNode is set to a empty linked list
        currentNode = self.linkedLists[hash_index]
        if currentNode.data == None and currentNode.data != data:   # Checking that there is a empty slot and also that it's not duplicate
            self.linkedLists[hash_index] = newNode                  # Inserting the data to the linked list to its first node
            return
        else:                               # If there's already data in the linked list it's going to this else
            while(currentNode != None):     # If the first node is not empty (None) there's already data in the linked list
                prevNode = currentNode
                if (currentNode.data == data): # Checking if it's duplicate, as if it is the new value is already in the list --> return 
                    return # print("Don't insert duplicates.\n")
                currentNode = currentNode.next
            prevNode.next = newNode
        return            

    # Deleting a value/item from the hash table
    def delete(self, data):
        hash_index = self.produceHash(data)             # Calling method that does the hash, so it gets the index for the value/string given
        currentNode = self.linkedLists[hash_index]      # This is the first node

        if (currentNode.data == data):                  # Checking if the data to be deleted is the first node of a linked list
            if (currentNode.next == None):              # If the first is none and also the only node in the list
                self.linkedLists[hash_index] = Node(None)   # It's made to a None (empty list) 
                return
            self.linkedLists[hash_index] = currentNode.next     # the next node is put to first node
            currentNode = None              
            return
        else:                               # If there's already data in the linked list it goes to this else
            prevNode = currentNode          
            currentNode = prevNode.next                                     
            while (currentNode != None):                # If the first node is not empty (None)      
                if (currentNode.data == data):              # When finding the right data it's deleted
                    prevNode.next = currentNode.next
                    currentNode = None
                    return print(f"Deleted '{data}' from the hash table.")
                prevNode = currentNode
                currentNode = currentNode.next
        return print(f"There isn't '{data}' to be deleted.")          # If there isn't a value to be deleted, error message is returned


    # Function for searching if a wanted value is in the hastable
    def search(self, data):
        hash_index = self.produceHash(data)         # Calling method that does the hash

        currentNode = self.linkedLists[hash_index] 

        while(currentNode != None):
            if (currentNode.data == data): 
                return print(f"Found '{currentNode.data}' from the hashtable.")  # If the element is found, message is returned
            currentNode = currentNode.next
        return print(f"'{data}' is not in the hashtable.\n")    # If the item is not found, error message is returned


    # Printing the linked structure (the hash table)
    def printing(self):
        print("")
        for i in range(self.tableSize):         
            currentNode = self.linkedLists[i]
        
            if (currentNode.data == None):  # If there is a list which first node is empty (the whole list is then empty)
                print("[]")         # printing this to show that there isn't anything on the linked list
                continue

            print("[ ", end="")         
            while(currentNode != None):         # While there is something in the list it prints the values this way
                print(currentNode.data, end=" ")     
                currentNode = currentNode.next
            print("]")
        print("")
        return

if __name__ == "__main__":
   
    table = hashTable(2)
    table.insert(12)            # Test with int
    table.insert("Testing")     # Test with string
    table.insert("Test")
    table.insert(12312476)
    table.insert("jhj32h4jh23k")
    table.insert("Testing")     # Testing with duplicate

    table.printing()

    table.search(12)                    # Test of data that is in the table 
    table.search("Not in the table")    # Test of something that isn't in the table

    table.delete("Test")                   # Test to delete data that is in the table
    table.delete("Not in the table")       # Test to delete data that is not in the table

    table.printing() 
