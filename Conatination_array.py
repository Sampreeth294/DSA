def conatination(nums:list[int])->list[int]:
    ans = []
    for i in range(len(nums)):
        ans.append(nums[i])
    for l in range(len(nums)):
        ans.append(nums[l])
    return ans

print(conatination([1,5,5,8,7,9]))