def fun(nums: list[int]) -> int:
    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1

nums = [1, 2, 2,4, 5, 6, 7, 8, 9, 10]
k = fun(nums)
print(nums[:k])