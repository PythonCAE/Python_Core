#Example 1:
a =[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
a = list(filter(lambda x: x>50,a))
print(a)



#Example 2:
def letter(arg):
    word =["a","e","i","o","u"]
    if arg in word:
        return True
    else:
        return False   
verbal =["a","e","g","j","p","f","t","r","z"]        
a=list(filter(letter,verbal))         
print(a)

#Using Lambda Function:
verbal1 =["a","e","g","j","p","f","t","r","z"]
a=list(filter(lambda x : True if (x in ["a","e","i","o","u"]) else False ),verbal1) 
print(a(verbal1))


