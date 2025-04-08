# Q.1) Write an anonymous function to calculate area of square.
square = lambda side: side*side
print(square(3))

# Q.2) Write a Python program to accept n elements in a set and find the length of a set, maximum, 
# minimum value and the sum of values in a set. (Don’t use built-in function)

n=int(input("enter the element:"))
my_set=set()
for i in range(n):
    element =int(input(f"enter the element{i+1}:"))
    my_set.add(element)
    length=len(my_set)
    max_value=max(my_set)
    min_value=min(my_set)
    sum_of_value=sum(my_set)
    print(f"lenght of set:{len}")
    print(f"maximum:{max_value}")
    print(f"minimum:{min_value}")
    print(f"sum of digit:{sum_of_value}")


