# Q.1) Write a Python program to unpack a tuple in several variables
tuple=(1,2,3,4,5)
a,b,c,d,e=tuple
print(a,b,c,d,e)

# Q.2) Write a Python program which accepts 6 integer values and prints “DUPLICATES” if any 
# of the values entered are duplicates otherwise it prints “ALL UNIQUE”. 
# Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed.
numbers = []
for i in range(5):
    num = int(input(f"Enter integer value {i + 1}: "))
    numbers.append(num)
if len(numbers) != len(set(numbers)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")
