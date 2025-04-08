# Q.1) Write an anonymous function to calculate area of square.
square= lambda side:side*side
print("area of square:",square(2))


# Q.2) Write a Python program to create a dictionary from a string. 
# Sample String: ’Hello all’ 
# Expected output: {'e': 1, 'o': 1, 'a': 1, 'l': 4, 'H': 1}
sample_string = 'Hello all'
char_count = {}
for char in sample_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)




