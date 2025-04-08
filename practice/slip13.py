# Q.1) Write a program which prints Fibonacci series of a number.
# n=int(input("enter the fibonacci series:"))
n=3
a,b=0,1
count =0
while(count<n):
    print(a,end="")
    temp = a
    a=b
    b=temp+b
    count += 1

# Q.2) Write a Python program to generate and print a dictionary that contains a number (between 
# 1 and n) in the form (x, x*x). 
# Sample Dictionary (n = 5) 
# Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

def squ_dict(n):
    return{x:x*x for x in range (1,n+1)}
n=5
square_dict=squ_dict(n)
print("square_dict:",square_dict)


