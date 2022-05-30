#Write a Python Program to write a content in File by using File_handling.
f=open("aa.txt","w")
a=input("Enter phone number")
b=input("Name")
c=input("Course name")
d=input("College name")
str=a+" "+b+" "+c+" "+d+"\n"
f.write(str)
f.close()