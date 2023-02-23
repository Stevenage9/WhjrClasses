import csv
data = []

with open("final.csv") as f:
    c = csv.reader(f)
    for i in c:
        data.append(i)

headers = data[0]
planet_data = data[1:]

for d in planet_data:
    d[2] = d[2].lower()
planet_data.sort(key = lambda planet_data:planet_data[2])

with open("sortedData.csv","a+") as f:
    c = csv.writer(f)
    c.writerow(headers)
    c.writerows(planet_data)

with open("sortedData.csv","a+") as input,open("sortedData.csv","w",newline="") as output:
    c=csv.writer(output)
    4