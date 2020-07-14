from random import *
str1="ABCDEFGHIJKLMNOPQRTUVWXYZ"
str2=str1.lower()
str3="%^&*!@#$"
str4="0123456789"
def intro():
    print("This is RANDOM PASSWORD GENERATOR , YOU ARE WELCOME!!")
    print("Enter password length of your choice:")
    print(UserInput())
def UserInput():
    upper=int(input("Number of upper case letters:"))
    lower=int(input("Number of lower case letters:"))
    spec=int(input("Number of special characters:"))
    num=int(input("Number of numberical values:"))
    return RanPasGen(upper,lower,spec,num)
def RanPasGen(upper,lower,spec,num):
    NewPassword=""
    if (upper+lower+spec+num)<6:
        print("Please enter minimum 6 letter Password.")
    else:
        for i in range(upper):
            NewPassword+=choice(str1)
        for x in range(lower):
            NewPassword+=choice(str2)
        for y in range(spec):
            NewPassword+=choice(str3)
        for z in range(num):
            NewPassword+=choice(str4)
    Password=list(NewPassword)
    shuff=shuffle(Password)
    newpass="".join(Password)
    return newpass
intro()  