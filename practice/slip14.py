# Q.1) Write a Python program to create a tuple of n numbers and print maximum, minimum, and 
# sum of elements in a tuple. 
n = int(input("Enter the number of elements in the tuple: "))
tuple_elements = tuple(int(input(f"Enter element {i+1}: ")) for i in range(n))
max_element = max(tuple_elements)
min_element = min(tuple_elements)
sum_elements = sum(tuple_elements)
print("Tuple:", tuple_elements)
print("Maximum element:", max_element)
print("Minimum element:", min_element)
print("Sum of elements:", sum_elements)

# Q.2) Write a Python program which accept an integer value ‘n’ and display all prime numbers 
# till 'n'

n = int(input("Enter an integer value: "))
print(f"Prime numbers up to {n}:")
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# ------DON'T UNDERSTAND BOTH PROGRAM--------