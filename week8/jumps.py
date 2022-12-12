# Algortihm to get the number of all possible ways to complete a game. 
# game has n levels, starting from level 0 and goal is to reach level n
# by jumping from a level to another; you're able to jump only to a or b levels higher

def jumps(n, a, b): #n=wanted level, a and b are jumps to be made
    wanted_level = n
    level = 0
    result = 0
    number_list = [0]

    while(n<1000):
    
        if number_list[level] < wanted_level:
            number_list.append(number_list[level]+a)
            number_list.append(number_list[level]+b)

        if level == len(number_list)-1:             
            break
            
        if number_list[level] == wanted_level:
            result = result +1

        level = level+1                                 

    return result

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937