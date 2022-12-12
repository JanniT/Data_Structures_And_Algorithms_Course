# Algorithm that returns a boolean True if triangle can be build and False if not. 

def triangle(a, b, c):
    
    if (a+b > c) and (a+c > b) and (b+c >a):    # It can be build if these are true
        return True
    else:
        return False  

if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True