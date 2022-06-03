import time
import os
import shutil

path = input("Enter the path of the directory to be sorted")
days = input("Enter the days")
 

time.time(days)

os.path.exists(path)
os.walk(path)
os.path.join()

ctime = os.stat(path).st_ctime


if ctime > days:
    os.remove(path)
else:
    shutil.rmtree()