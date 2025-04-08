# Q.1) Write a Python program to find the length of a string without using built-in function
# string = input("enter the string:")
string ="Dev"
length = 0
for char in string:
    length +=1
print(f"the length of a string:{length}")

 
# Q.2) Write a Python program to accept string and remove the characters which have odd index 
# values of a given string using user defined function.
text = "abcdef"
result = ""
for i in range(len(text)):
    if i % 2 == 0:  
        result += text[i]
print(result)  
