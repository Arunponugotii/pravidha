#!/usr/bin/env python
# coding: utf-8

# In[7]:


# A simple Python function

def fun():
    print("python classes")
		
# Driver code to call a function
fun()


# In[8]:


# A simple Python function to check
# whether x is even or odd


def ed(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
ed(2)
ed(3)


# In[13]:


# Python program to demonstrate
# default arguments


def Fun(x, y=30):
	print("x: ", x)
	print("y: ", y)


# Driver code (We call myFun() with only
# argument)
Fun(20)


# In[14]:


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)


# Keyword arguments
student(firstname='manasa', lastname='reddy')
student(lastname='reddy', firstname='manasa')


# In[17]:


# Python program to illustrate
# *args for variable number of arguments


def Fun(*argv):
	for arg in argv:
		print(arg)


Fun('Hello', 'Welcome', 'to', 'pythonclasses')


# In[1]:


# Python program to illustrate
# *kargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='manasa', mid='for', last='manasa')


# In[108]:


def square_value(num):
	"""This function returns the square
	value of the entered number"""
	return num**2


print(square_value(3))
print(square_value(-4))


# In[109]:


def fun():
    print("hello")
fun()


# In[110]:


# Here x is a new reference to same list lst
def myFun(x):
	x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


# In[111]:


def swap(x, y):
    temp = x
    x = y
    y = temp
    print(x)
    print(y)


# Driver code
x = 4
y = 5
swap(x, y)
print(x)
print(y)


# In[91]:


# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
	s = 'I love python'
	
	def f2():
		print(s)
		
	f2()

# Driver's code
f1()


# In[92]:


def plus(a,b):
  return a + b
  
# Create a `Summation` class
class Summation(object):
  def sum(self, a, b):
    self.c = a + b
    return self.c
# Instantiate `Summation` class to call `sum()`
x = Summation()
x.sum(1,2)


# In[112]:


def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World") 
  return 
  
hello()


# In[113]:


def run():
  for x in range(10):
     if x == 2:
       return x
  print("Run!")
  
run()


# In[118]:


def hello():
  print("Hello World") 

  return("hello")


def hello_noreturn():
    print("Hello World")
  
# Multiply the output of `hello()` with 2 
hello() * 2

#(Try to) multiply the output of `hello_noreturn()` with 2 
hello_noreturn() * 2


# In[119]:


# Define `plus()`
def plus(a,b):
  sum = a + b
  return (sum, a)

# Call `plus()` and unpack variables 
sum, a= plus(3,4)

# Print `sum()`
print(sum)


# In[35]:


def square(a):
    '''Returned argument a is squared.'''
    return a**a
print (square.__doc__)


# In[38]:


def some_function(argument1):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """

    return argument1

print(some_function.__doc__)


# In[121]:


#Default arguments
# Define `plus()` function
def plus(a,b = 2):
  return a + b
  
# Call `plus()` with only `a` parameter
plus(a=1)

# Call `plus()` with `a` and `b` parameters
#plus(a=1, b=3)


# In[120]:


#Define `plus()` with required arguments
def plus(a,b):
  return a + b
plus(1,2)


# In[122]:


#keyword arguments
# Define `plus()` function
def plus(a,b):
  return a + b
  
# Call `plus()` function with parameters 
plus(2,3)

# Call `plus()` function with keyword arguments
plus(b=2,a=1)


# In[123]:


# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  total = 0
  for i in args:
    total += i
  return total

# Calculate the sum  
plus(20,30,40,50,60)


# In[125]:


#Global vs Local Variables
# Global variable `init`
init = 1

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  # Local variable `sum()`
  total = 0
  for i in args:
    total += i
  return total
  
# Access the global variable
print("this is the initialized value " + str(init))

# (Try to) access the local variable
print("this is the sum " + str(total))


# In[57]:


#Anonymous Functions/lamda functions in Python
double = lambda x: x*2

double(5)


# In[61]:


# `sum()` lambda function
sum = lambda x, y: x + y;

# Call the `sum()` anonymous function


# "Translate" to a UDF
def sum(x, y):
  return x+y
sum(2,3)


# In[62]:


# anonymous functions are used while working with filter(),map()and reduce()
from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)


# In[126]:


#using main as a function
# Define `main()` function
def main():
 # hello()
  print("This is a main function")

main()


# In[67]:


#__init__ function that initializes an instance of a class or an object. 
class Dog:
    """    
    Requires:
    legs - Legs so that the dog can walk.
    color - A color of the fur.
    """

    def __init__(x, legs, color):
        x.legs = legs
        x.color = color
        
    def bark(x):
        bark = "bark" * 2
        return bark

if __name__ == "__main__":
    dog = Dog(4, "brown")
    bark = dog.bark()
    print(bark)


# In[69]:


# Python code to demonstrate
# call by value


string = "ravi"


def test(string):
	
	string = "ramu"
	print("Inside Function:", string)
	
# Driver's code
test(string)
print("Outside Function:", string)


# In[70]:


# Python code to demonstrate
# call by reference


def add_more(list):
	list.append(50)
	print("Inside Function", list)

# Driver's code
mylist = [10,20,30,40]

add_more(mylist)
print("Outside Function:", mylist)


# In[74]:


def add(a):
    return(a + 1)

def add2(c):
    return(c + 2)

output = add(add2(0))
#Pass `0` to `add_2` and pass result to `add_1`

print(output)


# In[ ]:




