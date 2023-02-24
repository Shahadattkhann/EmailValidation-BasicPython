email = input("Please Enter Your Email: ")
x,y,z = 0,0,0
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
                                print("Invalid Email, Email must not contain any upper letter, please remove upper letters from your Email")
                                x = 1
                         elif i==" ":
                             print("Invalid email, Email must not contain any spaces, please remove all the spaces in your Email")
                             y = 1
                         else:
                             print("Invalid Email, Email must not contain any special character")
                             z = 1 
                     if x==1 or y==1 or z==1:
                         print("Please correct your email and try again ")
                     else:
                         print("Valid email")              
             else:
                 print("Invalid Email, Email must contain . from last 3 or 4 index, ex: .com, .in")
         else:
             print("Invalid Email, Email must contain '@' only once. remove all extra @ from Your Email")
    else:
        print("Invalid Email, Email must contain 1st letter as an Alphabet")
else:
    print("Invalid Email, Email Length is too Short, lenth must be greter than 6")

