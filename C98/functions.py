myfile=open("test.txt","w+")
str1="This is the first line of the file"
myfile.write(str1)
myfile.close()
myfile2=open("test.txt",'r')
string=myfile2.read()
print(string)
#with open("test.txt", "r") as a: data_a = a.read()