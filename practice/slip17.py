
# Q.1) Write a Python program to accept and convert string in uppercase or vice versa. 
a="dev"
print(a.upper())

# Q.2) Write a Python program to display the following pattern (Floyd's triangle) 
# For n=3 
# 1 
# 2 3 
# 4 5 6 

n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
