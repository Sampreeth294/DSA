def function (nums:list[int])-> list[int]:
    target =0
    result = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == target:
                    triplet= sorted([nums[i],nums[j],nums[k]])

                    if triplet not in result:
                        result.append(triplet)
    return result



print(function([-1,0,1,2,-1,-4]))