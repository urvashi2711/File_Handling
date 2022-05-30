#Write a Python Program to check the frequency of "a" or "A" using file_handling.
f=open("ayuu.txt","r")
str=f.read()
c=0
for i in range(len(str)):
	if str[i]=="a" or str[i]=="A":
		c=c+1
print(c)
f.close()