# Q.1) Write a python program to check if a string is a Palindrome or not.
string=input("enter the string:")
string=string.lower()
string=string.replace("","")
if string == string[::-1]:
    print("this is a palindrome")
else:
    print("this is not palindrome")

# Q2.Write a Python program which finds sum of digits of a number. [20 M] 
# Example n=135 then output is 9 (1+3+5). 
n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(f"The sum of digits is {sum_digits}")