#Q.1- Write a python code to find a valid email address from a text.
import re
a=input("enter ur email")
j=0
b=re.finditer("^[a-zA-Z]{1}[_a-zA-Z0-9.]*[@]{1}['gmail.com''yahoo.com']{9,9}$",a)
for m in b:
    j=m.group()
if a==j:
    print("email is valid")
else:
    print("email is not valid")
#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
a=input("enter ur phone no")
j=0
b=re.finditer("^[+]{1}[9]{1}[1]{1}[6789]{1}\d{9}$",a)
for m in b:
    j=m.group()
if a==j:
    print("phone is valid")
else:
    print("phone is not valid")
