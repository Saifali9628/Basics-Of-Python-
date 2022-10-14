#Relational Operators
'''Relational operator ar used to evaluate conditions inside the if statements some examples of relational operators are:
(==)=Equal
(>=)=Greater than/equal to 
(<=)= less than /equal to ''' 

#logical operators
''' In python logical operators operate on conditional statements example:
(and) = true if both operands are true else false
(or) = true if at least one operand is true else false 
(not) = inverts true to false &false to'''

#and
age = int(input("Enter your age: "))
if(age>34 and age<56):
    print("you can work with us")
else:
    print("Sorry you can not work with us")
#or
age = int(input("Enter your age: "))
if(age>34 or age<56):
    print("you can work with us")
else:
    print("Sorry you can not work with us")
    