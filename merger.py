import csv
dataset1=[]
dataset2=[]

with open("archived.csv","r") as f:
    c=csv.reader(f)
    for i in c:
        dataset1.append(i)

with open("sortedData.csv","r") as f:
    c=csv.reader(f)
    for i in c:
        dataset2.append(i)

header1=dataset1[0]
planetdata1=dataset1[1:]

header2=dataset2[0]
planetdata2=dataset2[1:]

headers=header1+header2
planetdata=[]

for index,data in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("finalfinal.csv","a+") as f:
    c=csv.writer(f)
    c.writerow(headers)
    c.writerows(planetdata)