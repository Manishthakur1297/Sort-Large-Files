import os
from random import randint

size_mx = 2147483649    #2GB
curr_size = 0

print(os.getcwd())

file_path = r'C:\Users\m_manish\Desktop\LargeFile\file.txt'

if not os.path.exists(file_path):
    with open(file_path, 'w'):
        pass

with open(file_path,'a+') as f:
    while(curr_size<size_mx):
        curr_size = os.path.getsize(file_path)
        f.write(str(randint(-10000,10000)) + " ")
            