import os
import shutil
source=input("Path of source folder (with forward slashes): ")
print("If destination folder not already made, enter name for it")
destination=input("Destination folder: ")

if destination.find("/") !=-1:
    shutil.copytree(source, destination)
else:
    destinationTemp=destination
    os.mkdir("C:/"+destination)
    destination="C:/"+destination
    shutil.copytree(source, destination)