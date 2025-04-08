# Q1.Write a Python function to check whether a number is in a given range.
def range(number,start,end):
    return(number<=start<=end)
print(range(1,3,4))
print(range(2,5,4))



# Q.2) Write a Python program to find set difference, union, intersection and symmetric 
# difference.
a = {1,2,3,4}
b = {4,6,7,8}
print("difference:",a-b)
print("union:",a|b)
print("intersection:",a&b)
print("symmetric difference:",a^b)