def build_array_from_Permutation(nums:list[int]) -> list[int]:
    ans= []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans
print(build_array_from_Permutation([2,0,3,1]))
