def fun(s:str)->int:
    words = s.split()
    return len(words[-1])

print(fun('hello world sampreeth'))
