email = input("Please Enter Your Email: ")
d = 0
if len(email)>6:
    if email[0].isalpha():
         if "@" in email and email.count("@")==1:
             if (email[-4]==".")^(email[-3]=="."):
                 
                     for i in email:
                         if i.isdigit():
                             continue
                         elif i == "." or i == "_" or i=="@":
                             continue
                         elif i.isalpha():
                             if i==i.upper():
                                print("Invalid Email, Email must not contain any upper letter")
                         elif i==" ":
                             print("Invalid email, Email must not contain any spaces")
                         else:
                             print("Invalid Email, Email must not contain any special character")    
                     print(f"{email} is Valid")              
             else:
                 print("Invalid Email, Email must contain . from last 3 or 4 index")
         else:
             print("Invalid Email, Email must contain '@' only once.")
    else:
        print("Invalid Email, Email must contain 1st letter as an Alphabet")
else:
    print("Invalid Email, Email Length is too Short")

