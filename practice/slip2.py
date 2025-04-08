# Q.1) Write a Python program to get the 4th element from front and 4th element from last of a 
# tuple

tuple = (1,2,3,4,5,6,7)
front_tuple =tuple[4]
last_tuple = tuple[-4]
print(front_tuple)
print(last_tuple)


# Q.2) Write a Python program to perform given operations on set. [20 M] 
# a. check whether 2 sets are equal or not 
# b. Symmetric difference 
# c. Intersection of sets 
# d. Find maximum and the minimum value in a set. 

a ={1,2,3,4}
b ={5,6,7,4}
print("set a & set b are equal?:",a==b)
print("symmetric difference:",a^b)
print("intersection:",a&b)
max_value = max(a)
min_value = min(a)
print("maximum value in set a:",max_value)
print("minimum value in set a:",min_value)

















