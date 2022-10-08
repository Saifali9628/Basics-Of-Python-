letter=''' Dear <|name|>,Greetings from  Tesla .I am Happy to tell you about Your Selection 

                    you are Selected!
Have a Great Day ahead!
Thanks and Regards
Elon Musk
                    
                            <|Date|>'''
name=input("Enter Your Name:-\n")
date=input("Enter Date:-\n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)