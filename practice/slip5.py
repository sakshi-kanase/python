# Q.1) Write a Python program to sort the tuple T=(4,2,6.8,1.8,10) 
t = (4,2,6.8,1.8,10)
sorted_tuple = sorted(t)
print("sorted tuple:",sorted_tuple)


 
# Q.2) Write a function to calculate the sum of numbers from 0 to n.
def sum(n):
    return n*(n+1)//2
n=10
result = sum(n)
print(f"the sum of number from 0 to n:{result}")