import csv

sampleFile1 = open('data/demo54.csv')

reader = csv.reader(sampleFile1)
data = list(reader)
sampleFile1.close()

print(type(data))

for row in data:
    #print(row)
    for col in row:
        print(col, end=" ")
    print()