import math
import csv

with open('data.csv',newline='')as f:
        reader = csv.reader(f)
        file_data = list(reader)

data = file_data[0]

def mean(data):
        totalScore = 0
        totalLength = len(data)
        for x in data:
                totalScore+=int(x)
                
        mean = totalScore/totalLength
        return(mean)

squaredlist = []
for number in data:
        a = int(number)-mean(data)
        a = a**2
        squaredlist.append(a)

sum = 0
for i in squaredlist:
        sum+=i

result = sum/(len(data)-1)
stddev = math.sqrt(result)
print(stddev)
