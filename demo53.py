FILE_NAME = "data/Python_Introduction"
FILE_NAME2 = "data/Clone1"
FILE_NAME3 = "data/Clone2"
s1 = open(FILE_NAME, encoding='utf-8')
data1 = s1.read()
s1.close()
print(type(s1), type(data1), data1[:50])

with open(FILE_NAME, encoding='utf-8') as s2:
    data2 = s2.read()
print(type(data2), data2[50:100])

s3 = open(FILE_NAME2, "w", encoding='utf-8')
s3.write(data1)
s3.close()

with open(FILE_NAME3, "w", encoding='utf-8') as s4:
    s4.write(data2)