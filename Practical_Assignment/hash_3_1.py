import time

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

    # This reads the wanted file and inserts it contents to the hash table
    def readingFile(self,file): 
        file_r = open(file, "r")    
        
        for line in file_r:     
            self.insert(line)   # Inserting every line of the file to the hash table 

        file_r.close()
        return

    # This compares the hash tables words to given files words and counts duplicates
    def finding_matches(self,file): 
        file_r = open(file, "r")
        counter = 0
        for line in file_r:                     # Checking if a line matches to a content of the hash table
            searchLine = self.search(line)      # Calling the search method to search the given data from the hash table
            if (searchLine == True):            
                counter +=1
        file_r.close()
        return print(f"There's '{counter}' matching words")
    

    # Inserting a data to the hashtable
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
                if (currentNode.data == data): # Checking if it's duplicate, as if it is the 'new' data is already in the list --> return 
                    return # print("Don't insert duplicates.\n")
                currentNode = currentNode.next
            prevNode.next = newNode
        return            

    # Deleting a data from the hash table
    def delete(self, data):
        hash_index = self.produceHash(data)             # Calling method that does the hash, so it gets the index for the value/string given
        currentNode = self.linkedLists[hash_index]      # This is the first node

        if (currentNode.data == data):                  # Checking if the data to be deleted is the first node of a linked list
            
            if (currentNode.next == None):              # If the first is none and also the only node in the list
                self.linkedLists[hash_index] = Node(None)   # It's made to a None (empty list) 
                return
            self.linkedLists[hash_index] = currentNode.next     # the next node is put to first node
            currentNode.data = None              
            return
        else:                                           
            while (currentNode != None):                # If the first node is not empty (=None)      
                prevNode = currentNode                  
                if (currentNode.data == data):              # When finding the value it's deleted, no message is returned
                    prevNode.next = currentNode.next
                    currentNode = None
                    return
                currentNode = currentNode.next
        return print(f"There isn't '{data}' to be deleted.\n")          # If there isn't a value to be deleted, error message is returned


    # Function for searching if a wanted data is in the hastable
    def search(self, data):
        hash_index = self.produceHash(data)         # Calling method that does the hash

        currentNode = self.linkedLists[hash_index]   

        while(currentNode != None):                 
            if (currentNode.data == data):          
                return True                         # When the match is found this returns True
            currentNode = currentNode.next
        return False                                # When there isn't a match this return False

    # Printing the linked structure (the hash table)
    def printing(self):
        for i in range(self.tableSize):         
            currentNode = self.linkedLists[i]

            if (currentNode.data == None):
                print("[]")         # printing this to show that there isn't anything on the linked list
                continue

            print("[ ", end="")
            while(currentNode != None):
                print(currentNode.data, end=" ")
                currentNode = currentNode.next
            print("]")
        print("")
        return

if __name__ == "__main__":
    
    table = hashTable(1000)
    table.readingFile("words_alpha.txt")
    table.finding_matches("kaikkisanat.txt")

    # start1 = time.time()
    # table = hashTable(10000)
    # end1 = time.time()
    # print(f"Time for initializing the hash table: {end1-start1}")
    
    # start2 = time.time()
    # table.readingFile("words_alpha.txt") 
    # end2 = time.time()
    # print(f"Time for reading a file and storeing them: {end2-start2}")

    # start3 = time.time()
    # table.finding_matches("kaikkisanat.txt")
    # end3 = time.time()
    # print(f"Time for finding matches: {end3-start3}\n")
