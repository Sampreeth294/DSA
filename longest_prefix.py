def longest_prefix(s:list[str])->str:
    prefix = s[0]
    for i in range(1,len(s)):
        while not s[i].startswith(prefix):
            prefix = prefix[:-1]
            if prefix == " ":
                return " "
    return prefix

print(longest_prefix(["flower","flow","flight"]))