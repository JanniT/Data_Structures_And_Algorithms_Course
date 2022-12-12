# Algorithm to get the minimum number of required changes. Performs in Θ(n) time
# The array A of n numbers must be modified so that no two consecutive integers are not the same. 

def changes(A):
    numb_change = 0
    max_lenght = 10**6
    number_limit = 10**3

    while (1 <= len(A) <= max_lenght):                      #Assigning the limit of maxium lenght
        for i in range(len(A)):
            if i == 0:                                      #Checking if the list is in the end of it
                continue
            
            if(1 <= A[i] <= number_limit):                  #Assigning the limit of possible integers

                if i + 1 < len(A):                          
                    numb_next = A[i+1]                      #Assigning the numbers that are needed to compare the numbers                      
                    numb_prev = A[i-1]

                    if A[i] == numb_prev:
                        A[i] = numb_next + numb_prev + 1
                        numb_change = numb_change + 1       #Adding one to the counter number as there's one change
                                                            #Also making this to the next number below
                    if A[i] == numb_next:   
                        A[i+1] = numb_next + numb_prev + 1
                        numb_change = numb_change + 1
        return numb_change
    else:
        return None
    
if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2 