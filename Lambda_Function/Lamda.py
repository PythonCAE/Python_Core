# def fun1(x,y):
#     def fun2(z):
#         Sum = x+y+z
#         return Sum
#     return fun2   
# a = fun1(10,20)
# print(a(30))        


# fun = lambda a=10,b=20   : lambda f: f+a+b
# a= fun()
# print(a(30))

# Python program to demonstrate
# nested lambda functions



square = lambda x: x**2
product = lambda f, n: lambda x: f(x)*n

ans = product(square, 2)(10)
print(ans)


#Example 2:
a = lambda x : True if x>20 else False
print(a(50))

#Example 3:
a =lambda x : x > 10 
print(a(50))

#Example 3:
a =[10,20,9,80,6,120,290,360,250,2,6,9,50,55,65,70]
b = list(filter(lambda x :  x>20 and x<90,a ))
print(b)

#Example 4:
converter = 