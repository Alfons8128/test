x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print(x)  # Accesses global variable
    print(y)  # Accesses local variable

my_function()
print(x)  # Works
print(y)  # Raises an error: 'NameError: name 'y' is not defined'
