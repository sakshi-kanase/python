 
# Q.1) Write a Python program to create tuple of n numbers, print the first half values of tuple in 
# one line and the last half values of tuple on next line.
n=int(input("enter the number"))
number=tuple(range (1,n+1))
mid=n // 2
print(*number[:mid])
print(*number[mid:])

 
# Q.2) Write a Python program which prints fibonacci series of a number. 

n=int(input("enter the number:"))
a,b=0,1
count=0
while(count<n):
    print(a,end="")
    temp=a
    a=b
    b=temp +b
    count +=1

