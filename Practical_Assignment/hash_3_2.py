import time 

class linearList: 
    def __init__(self): 
        self.list = []   

    # This reads the wanted file and inserts it contents to the list 
    def readingFile(self,file):  
        file_r = open(file, "r")     
        for line in file_r:      
            self.insert(line)   # Inserting every line of the file to the list  
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
        return print(f"\nThere's '{counter}' matching words") 

    # Inserting a data to the list 
    def insert(self, data):  
        while (data != None): 
            self.list.append(data)
            return   
        return          

    # Function for searching if a wanted data is in the list
    def search(self, data):
        for element in self.list:
            if(element == data):    # If there's a match this returns True
                return True
        return False               # When there isn't a match this return False 
    
     # Printing the list
    def printing(self): 
        for line in self.list:
            print(line, end="")
        return 

 
if __name__ == "__main__": 

    start1 = time.time() 
    list = linearList()
    end1 = time.time() 
    print(f"Time for initializing the list: {end1-start1}") 

    start2 = time.time() 
    list.readingFile("words_alpha.txt")  
    end2 = time.time() 
    print(f"Reading a file and storeing the content: {end2-start2}") 

    start3 = time.time() 
    list.finding_matches("kaikkisanat.txt") 
    end3 = time.time() 
    print(f"Time for finding matches: {end3-start3}\n") 