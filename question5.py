#Write a program to print all the longest word in list format.
f=open("ayush.txt","r")
str=f.read().split()
m=max(str,key=len)
maxi=[i for i in str if len(i)==len(m)]
print(maxi)