def function(nums:list[int])->int:
    seen = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
            count = 0
            for n in nums:
                if n == i:
                    count += 1
            if count > len(nums)//2:    
                return i

print(function([3,2,3]))