# Write a program to create a diciomery of hindi words with values as their english translations provide user with an option to look it up!

myDict={
   "kutta":"Dog",
   "billi":"cat",
   "gai":"cow",
   "chutiya":"amjad",
   "gayak":"bhuvan",
   "gayni":"aman",
   "tesla worker":"ashraf",
}
print("options are",myDict.keys())
a=input("Enter the Hindi Word\n")
print("The Meaning of your word is:",myDict[a])