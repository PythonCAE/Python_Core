a=tuple(range(1,6))
b = tuple(range(6,12))
c = tuple(range(12,16))
result = a+b+c
print(result)
print(id(result))
print(id(c))

d=list(range(1,6))
e = list(range(6,12))
f = list(range(12,16))
result1 = d+e+f
print(id(d))
print(id(result1)) # result have different memeory address 

