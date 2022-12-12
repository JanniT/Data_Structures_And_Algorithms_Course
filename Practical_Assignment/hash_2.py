import time
import random

class Node: 
    def __init__(self, data):   # Initializing the nodes
        self.data = data
        self.next = None

class hashTable:

    def __init__(self, M):
        self.tableSize = M              # Table size
        self.linkedLists = [Node(None) for i in range(self.tableSize)]     # Creating the (empty) list containing linked lists
 
    # Hash function
    def produceHash(self, data):        # Calculating the slot/index of the data
        sum = 0
        data = str(data)
        for i in data:
            sum += ord(i)**ord(i)       # Ord() gets the unicode for the characters
        # print(sum) 
        return sum % self.tableSize 
        

    # Inserting a item/value to the hashtable
    def insert(self, data):       
        hash_index = self.produceHash(data)  # Calling method that does the hash
        newNode = Node(data)
        currentNode = self.linkedLists[hash_index]
        if (currentNode.data == None) and (currentNode.data != data): # checking that there is a empty slot and also that it's not duplicate
            self.linkedLists[hash_index] = newNode
            # print(self.linkedLists[hash_index].data)
            return
        else: 
            while(currentNode != None):
                prevNode = currentNode
                if (currentNode.data == data): # Checking if it's duplicate, as if it is the new value is already in the list --> return 
                    return #print("Don't insert duplicates.\n")
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
                return  print(f"Deleted '{data}' from the hash table.")
            self.linkedLists[hash_index] = currentNode.next     # the next node is put to first node
            currentNode = None              
            return  print(f"Deleted '{data}' from the hash table.")
        else:     
            prevNode = currentNode 
            currentNode = prevNode.next                                     
            while (currentNode != None):                # If the first node is not empty (None)      
                if (currentNode.data == data):              # When finding the value it's deleted
                    prevNode.next = currentNode.next
                    currentNode = None
                    return print(f"Deleted '{data}' from the hash table.")
                prevNode = currentNode
                currentNode = currentNode.next
        return print(f"There isn't '{data}' to be deleted.") 


    # Function for searching if a wanted value is in the hastable
    def search(self, data):
        hash_index = self.produceHash(data)         # Calling method that does the hash

        currentNode = self.linkedLists[hash_index] 

        while(currentNode != None):     #Checking that the first node of a linked list is not empty
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
            while(currentNode != None):     # While there is something in the list it prints the values this way
                print(currentNode.data, end=" ")
                currentNode = currentNode.next
            print("]")
        print("")
        return


if __name__ == "__main__":
    # Part 1.
    table = hashTable(3)
    table.insert(12)
    table.printing()

    table.insert("hashtable")
    table.printing()

    table.insert(1234)
    table.printing()

    table.insert(4328989)
    table.printing()

    table.insert("MMMM3")
    table.printing()

    table.insert(-12456)
    table.printing()

    table.insert("aaaabbbbcccc")
    table.printing()

    # Part 2.
    table.search(-12456)
    table.search("hashtable")
    table.search(1235)

    # Part 3. 
    table.delete("MMMM3")
    table.delete(1234)
    table.delete("aaaabbbbcccc")
    table.printing()

    end = time.time()

    # The time measurement for inserting 10 values
    # Via chancing the value in the for loop I tried this up to 1million

    # table = hashTable(500)
    # start = time.time()
    # for i in range(0, 10):
    #     table.insert(random.randint(0, 5000000000))
    # end = time.time()
    # print(f"Execution time of inserting: {end-start}\n")
