# Creating an empty set
b= set() 
print(type(b))
# adding values to an empty set
b.add(4)
b.add(5)
b.add(6)
b.add(6) #adding a value repeaedly does not changes a set 
b.add(8)
b.add(9)
b.add(10)
b.add(11)
# b.add([4,5,6]) we did't add list vlaue in a set becouse it is a unhasable list .
b.add((4,7,9)) # we use tuple in a set
#b.add({4:5})  #cannot add list or dictionary to sets
print(b)

print(len(b)) # print the length of this set
b.remove(5) # for remove the value form a set
print(b)

print(b.pop()) #pop the random value
print(b.clear()) #clear the all value in the set

