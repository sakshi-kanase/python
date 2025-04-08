# Q.1) Write a Python program to print average of all elements of sets.
n = [1,2,3,4,5]
avg = sum(n)/len(n)
print(avg)

# Q.2) Write a Python function to multiply all the numbers in a list. [20 M] 
# Sample-List: (8, 2, 3, -1, 7) 
# Expected Output: -336 

def multiply_list(number):
    result = 1
    for num in number:
        result *= num
    return result
sample_list = (8,2,3,-1,7)
print(multiply_list(sample_list))


