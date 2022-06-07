import os
from pprint import pprint
import time
print(os.getcwd())
pprint(os.listdir())
path1 = "中文測試目錄"
print(os.mkdir(path1))
os.chdir(path1)
print(os.getcwd())
time.sleep(10)
os.chdir("..")
os.rmdir(path1)
print("process terminated")