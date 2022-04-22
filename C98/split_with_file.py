#open file and save it to "filevar"
textfile=open("test.txt","r")
filevar=textfile.read()

#split "filevar",find length
aftersplit=filevar.split( )
length=len(aftersplit)
print("There are ",length," words in the file")