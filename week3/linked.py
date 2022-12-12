# Basic implementation of a linked list data structure in Python

class Node:

    def __init__(self, data):
        self.data = data                # contains the data
        self.next = None                # contains the reference to the upcoming node

class LinkedList:                       # Class that does the upkeep of the structure.

    def __init__(self):
        self.head = None                # Linkedlists start
        self.len = 0                    # Lenght of the linked list


    # Adds data to the end of the linked list
    def append(self, data):             
        newNode = Node(data)

        if self.head is None:           # Putting the data to new node and if the linkedlist is empty
            self.head = newNode         # making the newNode as head
            self.len += 1                  
            return
        
        latest = self.head              # Otherwise if there is already stuff in the list, the next item is 
        while (latest.next):            # appended to the end of the list
            latest = latest.next
        
        latest.next = newNode
        self.len += 1
        return None

    # inserting the new node containing the data to the wanted position 
    def insert(self, data, givenIndex):         
        index = 0                               
        newNode = Node(data)
        latest = self.head

        while(latest != None):

            if (givenIndex == 0):           
                newNode.next = self.head
                self.head = newNode
                self.len += 1 
                return

            elif (index == givenIndex):
                newNode.next = prevNode.next
                prevNode.next = newNode
                self.len += 1 
                return

            prevNode = latest
            latest = latest.next
            index += 1
        return None 

    # deleting wanted node from the list       
    def delete(self, givenIndex):               
        index = 0
        latest = self.head 

        while(latest != None):

            if (givenIndex == 0):
                self.head = latest.next
                self.len -= 1
                return
            
            elif (givenIndex == index):
                prevNode.next = latest.next
                self.len -= 1
                return

            prevNode = latest
            latest = latest.next
            index += 1

        return None 

    # searching a node from the wanted position which is indicated by the index
    def index(self, data):              
        index = 0                       
        last = self.head

        while(last != None):
            if (last.data == data):
                return index

            index +=1
            last = last.next
        return -1

    # Prints the linked list
    def print(self):                    
        temp = self.head
        for index in range(0, self.len):
            if(index == (self.len)-1):
                print(temp.data)
            else:
                print(temp.data, end=" -> ")
            temp = temp.next 
        return None

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    print(L.index(1))   # 1
    L.delete(0)
    L.print()           # 1 -> 10 -> 3          