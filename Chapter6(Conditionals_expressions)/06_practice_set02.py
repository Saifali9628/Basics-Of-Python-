# Write a  program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass assume 3 subject and take marks as an inout from the user 

hindi=int(input("Enter Hindi Marks: "))
english=int(input("Enter Hindi Marks: "))
science=int(input("Enter science Marks: "))
if (hindi<33 or english<33 or science<33):
 print("YOur are fail because you have less than 33% in one of the subjects")


elif (hindi<44+english<44+science<44)/3 >40:
    print("your are fail due to total percentage less than 40") 
else:
    print("Congratulations! you passed the exam")
    