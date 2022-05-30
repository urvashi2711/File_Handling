#Write a program to write in text file and it also check if an error occurs .
import sys as s
f=open("aaa.txt","r")
s1=f.readline()
s2=f.readline()
s3=f.readline()
s.stdout.write(s1)
s.stdout.write(s2)
s.stdout.write(s3)
s.stderr.write("No error found")
f.close()
