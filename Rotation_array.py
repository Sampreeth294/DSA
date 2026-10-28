
def function(nums: list[int], k: int) -> None:
    n = len(nums)

    k %= n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
function(nums, 3)
print(nums)
