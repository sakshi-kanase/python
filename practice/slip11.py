# #  Q.1) Write a Python program to accept the strings which contains all vowels. 
user_input=input("enter the string:")
vowels=set("aieou")
char_set=set(user_input)
if vowels.issubset(char_set):
    print("the string contains all vowels")
else:
    print("the string does not contain all vowels")

     
 # Q.2) Write a Python program to reverse a given number. 

num=int(input("enter the number:"))
reversed_number=int(str(num)[::-1])
print(f"the reversed number is:{reversed_number}")


