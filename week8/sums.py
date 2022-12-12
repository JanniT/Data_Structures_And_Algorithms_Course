# Algorithm to compute the number of all different sums 

def sums(items):

    number_list = [[]]
    result_list = []

    for subset in items: 
        number_list = number_list + [number + [subset] for number in number_list]

    number_list.pop(0)

    for n in number_list:       
        result_sum = 0
        for i in range(0,len(n)): 
            result_sum = result_sum + n[i]
            if result_sum not in result_list:
                result_list.append(result_sum)

    result = len(result_list)
    return result

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
    print(sums([2,3,4,5])) 