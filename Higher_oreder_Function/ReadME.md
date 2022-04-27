# Higher Order Function:
A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with another function are known as Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes functions as a parameter or returns a function as a result. Python too supports the concepts of higher order functions.

## Properties of higher-order functions:

A function is an instance of the Object type.
.You can store the function in a variable.
.You can pass the function as a parameter to another function.
.You can return the function from a function.
.You can store them in data structures such as hash tables, lists, …

## Functions as objects

In Python, a function can be assigned to a variable. This assignment does not call the function, instead a reference to that function is created. Consider the below example, for better understanding.

## Example:
```python
  # Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()
	
print(shout('Hello'))
	
# Assigning function to a variable
yell = shout
	
print(yell('Hello'))

```

## OUTPUT
```
HELLO
HELLO
```

## Passing Function as an argument to other function

Functions are like objects in Python, therefore, they can be passed as argument to other functions. Consider the below example, where we have created a function greet which takes a function as an argument.

```python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()
	
def whisper(text):
	return text.lower()
	
def greet(func):
	# storing the function in a variable
	greeting = func("Hi, I am created by a function \
	passed as an argument.")
	print(greeting)
	
greet(shout)
greet(whisper)

```
