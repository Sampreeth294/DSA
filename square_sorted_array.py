def function(nums:list[int])-> list[int]:
    result = []
    for i in nums:
        result.append(i*i)
    return sorted(result)

print(function([-4,-1,0,3,10]))