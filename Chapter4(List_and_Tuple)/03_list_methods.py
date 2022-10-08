l1=[1,8,7,2,21,15]
# l1_sorted = l1.sort() #this is wrong mehtod to use 
l1.sort() #this is the right way to use this list
print(l1)
l1.reverse() #for reverse the list value
print(l1)

l1.append(45) #adds 45 at the end of the list
print(l1)

l1.insert(0,544) #means the value of 544 is inset into the index  0, if you want to insert the value into the index 1 then you type (1,544)
print(l1)
l1.insert(2,444)
print(l1)

l1.pop(2) #means  l1 is pop(remove) the the index value 2 
print(l1)

l1.remove(21) #where the value is 21 is remove from the list directaly here you never use the index value like(0,1,2),here use only the list number
print(l1)
