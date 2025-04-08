# Q.1) Write a Python program to print the set difference and a symmetric difference of two sets. 
a={1,2,3}
b={4,5,6}
print("set difference:",a-b)
print("symmetric difference:",a^b)

# Q.2) Write a Python program to create and display all combinations of letters, selecting each 
# letter from a different key in a dictionary. [20 M] 
# Sample data: {'1':['a','b'], 2':['c','d']} 
# Expected Output: 
# ac 
# ad 
# bc 
# bd 

import itertools
data = {'1':['a','b'],'2':['c','d']}
letter_combiniation=list(itertools.product(data['1'],data['2']))
for combination in letter_combiniation:
    print("".join(combination))