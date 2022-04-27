import os
import shutil
#os.mkdir("C:/Users/aqswe/Desktop/Desktop folders/Whitehatjr/Classes/C99/newfolderv")
#os.getcwd()

#path="c:/Users/aqswe/Desktop/Desktop folders/Whitehatjr/Classes/C99/file.py"
#isexsits=os.path.exists(path)
#print (isexsits)

#root_ext=os.path.splitext("c:/Users/aqswe/Desktop/Desktop folders/Whitehatjr/Classes/C99/file.py")
#print (root_ext)

#dir=os.listdir("C:/Users/aqswe/Desktop")
#print(dir)

#source="C:/Users/aqswe/Desktop/Desktop folders/Whitehatjr/Classes/C99/file.txt"
#destination="C:/Users/aqswe/Desktop/Desktop folders/Whitehatjr/Classes/C99/copy.txt"
#dest=shutil.copy(source,destination)

path=input("Name of folder to be backed: ")
listOfFiles=os.listdir(path)

for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext==' ':
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
        