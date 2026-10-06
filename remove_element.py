def fun (nums:list[int], val:int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i]=nums[j]
            i=i+1
    return i

nums = [3,2,2,3]
val = 3
print(fun(nums, val))