def richest(accounts:list[list[int]]) -> list[int]:
    wealth = 0
    for i in range(len(accounts)):
        total = 0
        for j in range(len(accounts[i])):
            total =total+ accounts[i][j]

            if total > wealth:
                wealth = total

    return wealth

print(richest([[1,2,3,4],[4,5,7,8],[8,7,9,4]]))