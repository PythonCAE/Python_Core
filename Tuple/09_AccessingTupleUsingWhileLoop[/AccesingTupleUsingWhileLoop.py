a = tuple(range(1,5))
b = tuple(range(11,15))
c = (a,6,7,8,9,10,b)
d = len(c)
i =0
while(d>i):
    if type(c[i]) is tuple:
        if(len(c[i])>1):
            e=len(c[i])
            j=0
            while(e>j):
                print(c[i][j])
                j += 1
    else:
        print(c[i])    
    i += 1      


a =[(10,20),(30,4)]
a.append((70,80))      
print(a)

a =([1,2,3],[4,5,6],[7,8,9])
a.append([10,11,12])
print(a)
