import csv

with open('Data2Sorted.csv', newline="") as f:
  reader = csv.reader(f)
  planetsData2 = list(reader)


with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  planetsData1 = list(reader)

headers1 = planetsData1[0]
planet_data1 = planetsData1[1:]
headers2 = planetsData2[0]
planet_data2 = planetsData2[1:]

headers = headers1 + headers2

planetData = []
count = 0
count1 = 1
for i in planet_data1:
    planetData.append(planet_data1[count] + planet_data2[count1])
    count = count + 1
    count1 = count1 + 2

print(planetData[0])
print(planetData[1])