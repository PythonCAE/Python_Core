a = {1,2,3,"Hello",4,5,"World"}
print(id(a))
# a.remove("Morning")
# a.discard("Morning")
a.remove(1)
a.discard(2)
print(a)
print(id(a))
