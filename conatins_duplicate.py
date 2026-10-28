def function(nums:list[int]) -> bool:
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

print(function([1,2,3,4,5,6,7,8,9,10]))