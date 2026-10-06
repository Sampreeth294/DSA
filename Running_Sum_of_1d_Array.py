def one_d_array(nums: list[int]) -> list[int]:
    ans = []
    total = 0
    for u in range(len(nums)):
        total = total+nums[u]
        ans.append(total)

    return ans

print(one_d_array([1,2,3,4,5,6,7,8,9,10]))