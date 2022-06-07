import os
from pprint import pprint
print(os.getcwd())
pprint(os.listdir())
print(os.mkdir("temp1"))
os.chdir("temp1")
print(os.getcwd())
pprint(os.listdir())