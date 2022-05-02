a = tuple(range(1,5))
b = tuple(range(11,15))
c = (a,6,7,8,9,10,b)
d =len(c)
# print(d)

for i in range(d):
    if type(c[i]) is tuple:
        if len(c[i]) >1:
            f = len(c[i])
            for j in range(f):
                print(c[i][j])
    else:
        print(c[i])            