def Reverse_string(s:list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right :
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1
    return s

print(Reverse_string(["j", "s", "a", "d", "w"]))