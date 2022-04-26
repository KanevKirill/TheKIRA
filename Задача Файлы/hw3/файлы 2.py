import glob
import os
import operator
from collections import OrderedDict


general_dir = 'General'
file_name = 'general.txt'
BASE_PATH = os.getcwd()
full_path = os.path.join(BASE_PATH, general_dir, file_name)


files = {}


for file_name in os.listdir('file_read'):
    file_line = []
    with open('file_read\\'+file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
           file_line.append(line)
    files[len(file_line)] = file_line
sorted_keys = sorted(files.keys())
with open(full_path, 'w', encoding='utf-8') as f:
    for keys in sorted_keys:
        f.write(''.join(files[keys]))