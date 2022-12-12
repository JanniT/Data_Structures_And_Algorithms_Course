# Implementing quicksort in Python. 

def qsortHelp(A, i, j):         # i = Start index, j = End index
    pivot = A[i]                #Choosing the pivot as the first index
    low = i + 1
    high = j

    while True:
        while (low <= high) and (A[high] >= pivot):     #if the value is larger than pivot it stays and we move to left
            high = high - 1

        while (low <= high) and (A[low] <= pivot):      #if the value is smaller than pivot it stays and we move
            low = low + 1
        
        if low <= high:                                 #There's value for high and low that are out of order or 
            (A[low], A[high]) = (A[high], A[low])       #or low is higher than high and then exit from the loop

        else: 
            break

    (A[i], A[high]) = (A[high], A[i])
    return high

def qsort(A, i, j):
    if (i < j):
        pi = qsortHelp(A, i, j)
        qsort(A, i, pi-1)
        qsort(A, pi+1, j)
  
if __name__ == "__main__":
    A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]