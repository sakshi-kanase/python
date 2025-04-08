# Q.1) Write a Python program to find the repeated items of a tuple.

tuple =(1,2,3,2,4,5,4)
seen_items=set()
repeted_items=set()
for item in tuple:
    if item in seen_items:
        repeted_items.add(item)
    else:
        seen_items.add(item)
print("repeated items in tuple:",repeted_items)

 
# Q.2) Write a Python program to create a set with any 3 weekdays. Add single element to the set 
# and print it. Add multiple elements and print the set. 

weekdays = {"monday","tuesday","wednesday"}
weekdays.add("thursday")
print("after adding the single elements:",weekdays)
weekdays.update({"friday","saturday","sunday"})
print("after adding multiple elements:",weekdays)




