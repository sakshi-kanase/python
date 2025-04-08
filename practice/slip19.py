# Q.1) Write a Python program to calculate the average of numbers in a given list. 
n={1,2,3,4,5}
avg=sum(n)/len(n)
print(avg)

# Q.2) Write a program to display following pattern. [20 M] 
# 1 2 3 4 
# 1 2 3  
# 1 2   
# 1  

n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")   
    print()