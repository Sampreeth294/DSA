def two_sum(nums:list[int],target:int)->list[nums]:
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                #return nums[i],nums[j]
                return [i,j]

print(two_sum([2,8,5,4,2,7,7],14))