# Q.1) Write an anonymous function to calculate area of square.
square =lambda side:side*side
print(square(2))

 
# Q.2) Write a Python program which finds sum of digits of a number. [20 M] 
# Example n=130 then output is 4 (1+3+0).

n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(f"The sum of digits is {sum_digits}")
