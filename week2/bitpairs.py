# Algorithm to get the sum of distances. 
# The given bit string contains either zeros or ones. The algoritm counts the sum 
# of the distance of bit pairs where both bits are 1. 

def pairs(s):
    sum = 0
    max_lemght = 10**5
    if (len(s) <= max_lemght):

        for number in range(len(s)):
          
            if s[number] == "1":

                for number1 in range(number, len(s)):
                
                    if s[number1] == "1":
                        sum += (number1 - number)
                    
        return sum
    else: 
        return None
    
if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71