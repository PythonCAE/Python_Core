# def function1():
#     def function2():
#         print("Hello") 
#     return function2
# a = function1()
# print(a())  


# def function1(x):
#     def function2(y):
#         return x+y
#     return function2

# f1 = function1(10)
# print(f1(15))     
#

def fun1(argument):
    return argument.upper()

def fun2(argument):
    return argument.lower()   

def function(arg):
    return arg("Hello How are you!!!")
a = function(fun1)
print(a)          