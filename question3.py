#Write a Python Program to write lines in text file .
f=open("student.txt","w")
a=["Ayush\n","Kumar\n","Upadhyay\n"]
f.writelines(a)
f.close()