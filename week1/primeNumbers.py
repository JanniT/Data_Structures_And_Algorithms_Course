# Algorithm to get primenumbers that are less or equal to N.
def primes(N):
    numberList=[] # Creating list for all the primenumbers

    number = 10**5
                
    if(1 <= N <= number):
        for i in range(2, N+1):
            for j in range(2, int(i ** 0.5) + 1):
                if (i % j) == 0:
                    break
            else:
                numberList.append(i) 
    else:
        print("Check the number you gave.")  
    return len(numberList)

if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15