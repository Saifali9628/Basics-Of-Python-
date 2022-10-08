''' Operator in Python
1- Airthmatic Operators (+,-,*,/ etc)
2-Assignment Operators(=.+=,-=, etc)
3-Comporison Operators(==,>,<, >=, !=, etc)
Logical Operators (and,Or,not) '''

a=3
b=4
#Airthmatics Operators
print("the value of 3+4 is",3+4)
print("the value of 3-4 is",3-4)
print("the value of 3*4 is",3*4)
print("the value of 3/4 is",3/4)

#Assignmet operators
a=34
a-=2 # += नंबर को जोड़ देता है 
a*=2# गुणा करने के लिए 
a/=2
print(a)

#compersion operators
b=(4>7)
print(b)# ये false प्रिन्ट करेगा क्यू की ये गलत है ये operatos boolian को represent करता है 
c= (14>=7) # >= का मतलब (or) होता है । और ये ture print करेगा 
d = (14>=7)
E= (14<=7)
f= (14==7) #== का मतलब बराबर होता है अगर 14 और 7 बराबर है तो ही true प्रिन्ट होगा नहीं तो false प्रिन्ट होगा  
g =(14!=7) #!= (Not equal to) 
print(c)
print(d)
print(E)
print(f)
print(g)

#logical Operators ये हमेशा boolian के साथ use होता है 
bool1 =True
bool2 =False

print("the value of bool1 and bool2 is",(bool1 and bool2)) # (And ) तब true print करेगा जब दोनों variable true हो 
print("the value of bool1 and bool2 is",(bool1 or bool2)) # (or) दोनों मे से कोई एक true हो जाए तो true print करेगा 
print("the value of bool1 and bool2 is",(not bool2)) #not operator हमेशा एक vaiabele के साथ use होता है  ये उल्टा कर देता है ture को false एण्ड false को true कर देगा 

