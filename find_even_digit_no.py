def fun(nums:list[int]) -> list[int]:
    count =  0
    for i in range (len(nums)):
        if (len(str(nums[i]))%2 == 0):
            count += 1
    return count

print(fun([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))