def fun(candies:list[int],extraCandies:int)->list[bool]:
    result = []
    greatestCandies = max(candies)
    for i in range(len(candies)):
        if candies[i] >= greatestCandies:
            result.append(True)
        else:
            result.append(False)
    return result

print(fun([1,3,4,5,2],5))