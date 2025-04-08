# Q.1) Write a Python program to create a tuple using two different tuples. 
tuple1 = (1,2,3)
tuple2 =(4,5,6)
combine_tuple= tuple1 + tuple2
print("combine tuple:",combine_tuple)

 
# Q.2) Write a Python program to count the occurrences of each word in a given sentence. 
from collections import Counter
sentence = "This is a bag"
words =sentence.lower().split()
word_cout= Counter(words)
print("word occurrence:",word_cout)