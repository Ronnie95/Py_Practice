def my_function():
    print("Hello")

my_function()

def function(n1, n2):
    print(n1 + n2)

function(10, 10)

def add(n1, n2):
    return n1 + n2

result = add(2,4)
print(type(result))

def greet(name):
    print(f"Hello {name}")
    print(f"how you doing {name}")

greet("Ron")

def greet_with(name, number): # positional arguement
    print(f"Hello {name}")
    print(f"Your number is {number}")

greet_with("Ron", 12344334434)

def fun(a=1, b =2 ,c =4): #Keyword argument
    print(f"Hello {a},{b},{c}")

fun()