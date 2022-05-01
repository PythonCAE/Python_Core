a = []
for i in range(int(input("Enter The Length:"))):
    a.append(i)
    
print(a,type(a))
a = tuple(a) 
print(type(a),a)    
