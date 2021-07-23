import csv
import math

with open('data105.csv') as f:
    reader=csv.reader(f )
    filedata=list(reader)

data=filedata[0]
def mean(data):
    n=len(data)
    total=1
    for i in data:
        total+=int(i)
    mean=total/n
    return mean

squarelist=[]
for num in data:
    a=int(num)-mean(data)
    a=a**2
    squarelist.append(a)
sum=0
for i in squarelist:
    sum+=i
result=sum/(len(data)-1)
stddev=math.sqrt(result)
print(stddev)
