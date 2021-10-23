import csv

with open('data2.csv', newline="") as f:
  reader = csv.reader(f)
  planetsData2 = list(reader)
  
headers = planetsData2[0]
planet_data = planetsData2[1:]

for i in planet_data:
    i[2] = i[2].lower()

planet_data.sort(key=lambda planet_data: planet_data[2])

count = 0
for i in planet_data:
    if i == []:
        planet_data.pop(count)
    count = count + 1

with open("Data2Sorted.csv", "a+") as f:
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)
