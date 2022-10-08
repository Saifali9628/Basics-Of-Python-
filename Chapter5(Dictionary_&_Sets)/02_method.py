from tkinter import N


myDict = {
    "Fast": "In a Quick Manner",
    "Saif":"A coder",
    "Aman": "Good boy",
    "Amjad":"chutiya",
    "Reting":[3,5,4,1],
    "anotherdict":{'Saif':'player'},
    1:2
}
print(myDict.keys()) # this function is used to print the value in list with key
print(type(myDict.keys())) #when you see the type of the list then you think this is print the "list" but there is print the another type value "<class 'dict_key'"
print(list(myDict.keys())) # if you want to convert into the the list then you try this print value= print(list(myDict.keys()))
print(myDict.items()) #printes the (keys,value) for all content   of  the dicitornary
print(myDict)
updateDict ={    #if you want to upadate the Dicitornary then you will try 
    "Bhuvan":"Friend",
    "Ashraf":" Friend", 
    
}
myDict.update(updateDict) #update the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Saif")) # यहा हम print(myDict["Saif"]) ऐसे भी लिख सकते थे, Print(myDict.get("saif")) इस लिए लिखे है क्योंकि Print(myDict.get("saif")) अगर इसकी value Dictionry मे नहीं होगी तो उसकी value none print करेगा , 
print(myDict["saif2"]) #throws an error as saif2 is not present in the dictionary