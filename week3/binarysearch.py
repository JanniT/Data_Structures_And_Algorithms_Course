# Implementing the binary search in Python. Performs in Θ(log(n)) time.

import math

def search(A: list, item: int):
    middle_number = 0               
    smaller_number = 0              
    higher_number = len(A) -1       
    max_number = 10**6

    if (len(A) <= max_number):

        while(smaller_number <= higher_number):

            middle_number = math.floor((smaller_number + higher_number) / 2)

            if (0 <= A[middle_number]) and (A[middle_number] <= max_number):        #Setting the limit for integer values
                
                if A[middle_number] > item: 
                    higher_number = middle_number -1

                elif A[middle_number] < item: 
                    smaller_number = middle_number +1
                
                else: 
                    return middle_number
    return -1                                   #If the item is not found this returns -1

if __name__ == "__main__":
    A = [1, 2, 3, 6, 10, 15, 22, 27, 30, 31]
    print(search(A, 6))     # 3
    print(search(A, 7))     # -1
    print(search(A, 30))    # 8

